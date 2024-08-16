# ML Pipeline

このプロジェクトは、ユーザー固有のアイテム推薦のための機械学習パイプラインを実装しています。このパイプラインは、データの前処理、モデルのトレーニング、推論、結果のバリデーション、および結果の保存を行います。

## Getting Started

以下の手順に従って、ローカルマシンでプロジェクトをセットアップし、開発およびテストを行います。デプロイに関する情報は、後述のデプロイメントセクションを参照してください。

### Prerequisites

必要なソフトウェアとそのインストール方法

- Python 3.9+
- Poetry
- Docker (オプション)
- Prefect

### Installing

開発環境をセットアップするための手順

1. リポジトリをクローンします。

    ```sh
    git clone https://github.com/yourusername/ml_pipeline.git
    cd ml_pipeline
    ```

2. Poetryを使用して依存関係をインストールします。

    ```sh
    poetry install
    ```

### ローカルでパイプラインを実行

以下のコマンドでパイプラインを実行できます。

```sh
python -m ml_pipeline.pipeline --exec_date 2024-01-01
```

### Prefect Serverを起動してフローを確認

Prefect Serverを起動して、フローの実行状況を確認できます。

1. Prefect Serverを起動します。

    ```sh
    prefect server start
    ```

2. ブラウザで `http://localhost:4200` にアクセスして、ダッシュボードを確認します。

## Running the tests

自動化されたテストを実行する方法を説明します。

### End to Endテスト

これらのテストは、システム全体の動作を確認します。

```sh
# -s でログを表示
pytest
```

### コーディングスタイルのテスト

コードのスタイルをチェックするためのテストです。

```sh
flake8
black --check .
isort --check-only .
```

## Deployment

ライブシステムにデプロイする方法についての追加情報

このプロジェクトはDockerを使用してデプロイできます。以下のコマンドでDockerイメージをビルドし、コンテナを実行します。

```sh
docker build -t ml_pipeline .
docker run --rm ml_pipeline --exec_date 2024-01-01
```