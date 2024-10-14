# 1. ベースイメージ
FROM python:3.9-slim as builder

# 2. 作業ディレクトリの設定
WORKDIR /app

# 3. Poetryのインストール
RUN pip install poetry

# 4. 依存関係のインストール
COPY pyproject.toml ./
RUN poetry config virtualenvs.create false && poetry install --no-dev

# 5. ソースコードのコピー
COPY app/ app/
COPY tests/ tests/

# 6. テストの実行
# RUN poetry run pytest tests/

# 7. プロダクション用イメージ
FROM python:3.9-slim

WORKDIR /app

# 8. 依存関係のコピー
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /app/app /app/app

# 9. 起動スクリプト
CMD ["uvicorn", "app.presentation.main:app", "--host", "0.0.0.0", "--port", "8000"]