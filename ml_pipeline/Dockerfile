# syntax=docker/dockerfile:1

# ビルドステージ
FROM python:3.11-slim AS builder

# パッケージキャッシュの設定
RUN --mount=type=cache,target=/root/.cache/pip pip install --upgrade pip

# 作業ディレクトリの設定
WORKDIR /app

# 依存関係のインストール
COPY pyproject.toml ./
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install poetry && \
    poetry config virtualenvs.create false

# ソースコードのコピー
COPY . .

# 依存関係のインストール
RUN poetry install --only main

# 実行ステージ
FROM python:3.11-slim

# アプリケーションの作業ディレクトリ
WORKDIR /app

# ビルドステージから必要なファイルをコピー
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /app /app

# エントリーポイント
ENTRYPOINT ["python", "-m", "ml_pipeline.pipeline"]

# デフォルトのコマンド
CMD ["--exec_date", "2024-01-01"]