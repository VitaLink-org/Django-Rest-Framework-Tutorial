from django_filters import rest_framework as filters
from rest_framework import generics, status, views, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer

# Create your views here.


class BookCreateAPIView(views.APIView):
    # 本モデルの登録API

    def post(self, request):
        # 本モデルの登録APIに対応するハンドラメソッド

        # シリアライザオブジェクトを作成
        serializer = BookSerializer(data=request.data)

        # バリデーションを実行
        serializer.is_valid(raise_exception=True)

        # モデルオブジェクトを登録
        serializer.save()

        # レスポンスオブジェクトを作成して返す
        return Response(serializer.data, status.HTTP_201_CREATED)


class BookFilter(filters.FilterSet):
    # 本モデル用のフィルタクラス
    class Meta:
        model = Book
        fields = "__all__"


class BookListAPIView(views.APIView):
    # 本モデルの取得(一覧)APIクラス
    def get(self, request):
        # 本モデルの取得(一覧)APIに対応するハンドラメソッド

        # モデルオブジェクトをクエリ文字列を使ってフィルタリングした結果を取得
        filterset = BookFilter(request.query_params, queryset=Book.objects.all())

        if not filterset.is_valid():
            # クエリ文字列がNGの場合は400エラー
            raise ValidationError(filterset.errors)

        # シリアライザオブジェクトを作成
        serializer = BookSerializer(instance=filterset.qs, many=True)

        # レスポンスオブジェクトを作成して返す
        return Response(serializer.data)


class BookRetrieveAPIView(views.APIView):
    # 本モデルの取得(詳細)APIクラス
    def get(self, request, pk):
        # 本モデルの取得(詳細)APIに対応するハンドラメソッド

        # モデルオブジェクトを取得
        book = get_object_or_404(Book, pk=pk)

        # シリアライザオブジェクトを作成
        serializer = BookSerializer(instance=book)

        # レスポンスオブジェクトを作成して返す
        return Response(serializer.data)


class BookUpdateAPIView(views.APIView):
    # 本モデルの更新・一部更新APIクラス
    def put(self, request, pk):
        # 本モデルの更新APIに対応するハンドラメソッド

        # モデルオブジェクトを取得
        book = get_object_or_404(Book, pk=pk)

        # シリアライザオブジェクトを作成
        serializer = BookSerializer(instance=book, data=request.data)

        # バリデーションを実行
        serializer.is_valid(raise_exception=True)

        # モデルオブジェクトを更新
        serializer.save()

        # レスポンスオブジェクトを作成して返す
        return Response(serializer.data)

    def patch(self, request, pk):
        # 本モデルの一部更新APIに対応するハンドラメソッド

        # モデルオブジェクトを取得
        book = get_object_or_404(Book, pk=pk)

        # シリアライザオブジェクトを作成
        serializer = BookSerializer(instance=book, data=request.data, partial=True)

        # バリデーションを実行
        serializer.is_valid(raise_exception=True)

        # モデルオブジェクトを一部更新
        serializer.save()

        # レスポンスオブジェクトを作成して返す
        return Response(serializer.data)


class BookDestroyAPIView(views.APIView):
    # 本モデルの削除APIクラス
    def delete(self, request, pk):
        # 本モデルの削除APIに対応するハンドラメソッド

        # モデルオブジェクトを取得
        book = get_object_or_404(Book, pk=pk)

        # モデルオブジェクトの削除
        book.delete()

        # レスポンスオブジェクトを作成して返す
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookCreateGenericAPIView(generics.CreateAPIView):
    # 本モデルの登録APIクラス

    serializer_class = BookSerializer


class BookListGenericAPIView(generics.ListAPIView):
    # 本モデルの取得(一覧)APIクラス
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = "__all__"


class BookRetrieveGenericAPIView(generics.RetrieveAPIView):
    # 本モデルの取得(詳細)APIクラス
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateGenericAPIView(generics.UpdateAPIView):
    # 本モデルの更新・一部更新APIクラス
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDestroyGenericAPIView(generics.DestroyAPIView):
    # 本モデルの削除APIクラス
    queryset = Book.objects.all()


class BookViewSet(viewsets.ViewSet):
    # 本モデルのCRUD用APIクラス

    queryset = Book.objects.all()
    serializer_class = BookSerializer
