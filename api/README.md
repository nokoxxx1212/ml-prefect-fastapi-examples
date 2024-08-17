# Recommendation API README

## 概要
Recommendation APIは、ユーザーに対して推薦結果を提供するシンプルなAPIです。FastAPIを使用して構築されており、BigTableからデータを取得します。

## セットアップ

### 必要条件
- Python 3.9
- Poetry

### インストール手順

1. リポジトリをクローンします。
```
git clone <repository_url>
cd <repository_directory>
```

2. Poetryを使用して依存関係をインストールします。
```
poetry install
```

3. 必要に応じて、`config`ディレクトリ内の設定ファイルを編集します。

## 実行方法

### ローカル環境での実行
```
uvicorn src.presentation.main:app --reload
```

### Dockerを使用した実行
1. Dockerイメージをビルドします。
```
docker build -t recommendation-api .
```

2. Dockerコンテナを起動します。
```
docker run -p 8000:8000 recommendation-api
```

## エンドポイント

### GET /recommendations
指定されたユーザーIDに対する推薦結果を取得します。

#### リクエストパラメータ
- `user_id` (str): ユーザーID

#### リクエスト例
```bash
curl -X 'GET' \
  'http://localhost:8000/recommendations?user_id=test_user' \
  -H 'accept: application/json'
```

#### レスポンス
- 200 OK: 推薦結果を含むJSONオブジェクト
- 500 Internal Server Error: 推薦結果の取得に失敗した場合

#### レスポンス例
```json
{
  "recommendations": ["item1", "item2", "item3"]
}
```

## テスト
テストは`pytest`を使用して実行します。

```
poetry run pytest
```
