# Python公式イメージを使用（バージョンは必要に応じて変更）
FROM python:3.11

# 作業ディレクトリの作成と移動
WORKDIR /app

# ローカルのrequirements.txtをコピー
COPY requirements.txt .

# 必要なパッケージをインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリコードをすべてコピー
COPY . .

# コンテナ起動時に実行されるコマンド（例：REPL）
CMD ["python"]
