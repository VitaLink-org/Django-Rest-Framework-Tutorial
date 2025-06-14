from django.core.validators import RegexValidator
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Book


class BookSerializers(serializers.ModelSerializer):
    # 本モデル用のシリアライザ
    class Meta:
        # 対象のモデルを指定
        model = Book
        # 利用するフィールドを指定
        fields = ["id", "title", "price"]

        # 利用しないフィールドを指定
        # excludes = ["created_at"]

        validators = [
            UniqueTogetherValidator(
                queryset=Book.objects.all(),
                fields=("title", "price"),
                message="タイトルと価格でユニークになっていなければいけません",
            )
        ]
        extra_kwargs = {
            "title": {
                "validators": [
                    RegexValidator(r"^D.+$", message="タイトルは「D」で始めてください")
                ]
            }
        }

    def validate_title(self, value):
        # タイトルに対するバリデーション
        if "Java" in value:
            raise serializers.ValidationError(
                "タイトルには「Java」を含めないでください"
            )
        return value

    def validate(self, data):
        # 複数フィールド間のバリデーションメソッド
        title = data.get("title")
        price = data.get("price")
        if title and "薄い本" in title and price and price > 3000:
            raise serializers.ValidationError("薄い本は3000円を超えてはいけません")
        return data


class BookListSerializers(serializers.ListSerializer):
    # 複数の本モデルを扱うためのシリアライザ

    # 対象のシリアライザを指定　クラスではなくオブジェクトを指定
    child = BookSerializers()
