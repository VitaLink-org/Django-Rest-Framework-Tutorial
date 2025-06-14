from rest_framework import serializers

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


class BookListSerializers(serializers.ListSerializer):
    # 複数の本モデルを扱うためのシリアライザ

    # 対象のシリアライザを指定　クラスではなくオブジェクトを指定
    child = BookSerializers()
