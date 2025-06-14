import uuid

from django.db import models

# Create your models here.


class Publisher(models.Model):
    # 出版社モデル=1つの出版社に対して複数の本がある(多対一)
    class Meta:
        # テーブル名を publisher に設定
        db_table = "publisher"
        # 管理画面での表示名を 出版社に設定
        verbose_name = verbose_name_plural = "出版社"

    # このテーブルの主キーを設定
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # 二つ目のフィールドを文字列型で作成【カラム名：出版社名　格納できる最大文字列：20】
    name = models.CharField(verbose_name="出版社名", max_length=20)

    # 三つ目のフィールドを日時型(datetime型)で作成【カラム名：登録日時　データが作成されたときの日時が自動入力】
    created_at = models.DateTimeField(verbose_name="登録日時", auto_now_add=True)


class Book(models.Model):
    # 本モデル
    class Meta:
        # テーブル名を book に設定
        db_table = "book"
        # created_at の順に並び替え
        ordering = ["created_at"]
        # 管理画面でのテーブルの表示名を 本 に設定
        verbose_name = verbose_name_plural = "本"

    # このテーブルの主キーを設定【デフォルト：uuid　管理画面での値の変更ができなくなる】
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # 二つ目のフィールドを文字列型で作成【カラム名：タイトル　格納できる最大文字数：40　他のデータと同じ値は入らない】
    title = models.CharField(verbose_name="タイトル", max_length=40, unique=True)

    # 三つ目のフィールドを整数型(int型)で作成【カラム名：価格　値がnullや空白を許容する】
    price = models.IntegerField(verbose_name="価格", null=True, blank=True)

    # Publisherモデルとの多対一のリレーションを作成【カラム名：出版社　親テーブル(Publisherモデル)の該当データが削除されたときに、このデータも削除】
    publisher = models.ForeignKey(Publisher, verbose_name="出版社", on_delete=True)

    # 五つ目のフィールドを日時型(datetime型)で作成【カラム名：登録日時　データが作成されたときの日時が自動入力】
    created_at = models.DateTimeField(verbose_name="登録日時", auto_now_add=True)

    def __str__(self):
        # 管理画面でのこのデータの表示名を title に設定
        return self.title


class BookStock(models.Model):
    # 本の在庫モデル=本1種類ごとに一つのデータが作成される(1対1)
    class Meta:
        # テーブル名を book_stock に設定
        db_table = "book_stock"
        # 管理画面での表示名を 本の在庫 に設定
        verbose_name = verbose_name_plural = "本の在庫"

    # Bookモデルとの1対1のリレーションを作成【カラム名：本　親テーブル(Bookモデル)の該当データが削除されたときに、このデータも削除】
    book = models.OneToOneField(Book, verbose_name="本", on_delete=models.CASCADE)

    # 二つ目のフィールドを整数型(int型)で作成【カラム名：在庫数　デフォルトの値は0】
    quantity = models.IntegerField(verbose_name="在庫数", default=0)
