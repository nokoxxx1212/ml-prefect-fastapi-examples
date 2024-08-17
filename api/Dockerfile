# 1. ベースイメージ
FROM python:3.9-slim as builder

# 2. 作業ディレクトリの設定
WORKDIR /app

# 3. Poetryのインストール
RUN pip install poetry

# 4. 依存関係のインストール
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false && poetry install --no-dev

# 5. ソースコードのコピー
COPY src/ src/
COPY config/ config/
COPY tests/ tests/

# 6. テストの実行
RUN poetry run pytest tests/

# 7. プロダクション用イメージ
FROM python:3.9-slim

WORKDIR /app

# 8. 依存関係のコピー
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /app/src /app/src
COPY --from=builder /app/config /app/config

# 9. 起動スクリプト
CMD ["uvicorn", "src.presentation.main:app", "--host", "0.0.0.0", "--port", "8000"]
