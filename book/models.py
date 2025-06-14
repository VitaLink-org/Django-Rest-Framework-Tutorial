import uuid

from django.db import models

# Create your models here.


class Book(models.Model):
    class Meta:
        db_name = "book"
        ordering = ["created_at"]
        verbose_name = verbose_name_plural = "本"

    # このテーブルの主キーを設定【デフォルト：uuid　管理画面での値の変更ができなくなる】
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # 二つ目のフィールドを文字列型で作成【カラム名：タイトル　格納できる最大文字数：40　他のデータと同じ値は入らない】
    title = models.CharField(verbose_name="タイトル", max_length=40, unique=True)

    # 三つ目のフィールドを整数型(int型)で作成【カラム名：価格　値がnullや空白を許容する】
    price = models.IntegerField(verbose_name="価格", null=True, blank=True)

    # 四つ目のフィールドを日時型(datetime型)で作成【カラム名：登録日時　データが作成されたときの日時が自動入力】
    created_at = models.DateTimeField(verbose_name="登録日時", auto_now_add=True)

    def __str__(self):
        # 管理画面でのこのデータの表示名を title にする
        return self.title
