import argparse
import pandas as pd
from prefect import flow, task
from datetime import datetime
from .tasks.preprocess import preprocess
from .tasks.train import train
from .tasks.infer import infer
from .utils.logger import get_logger
from .utils.file_storage import save_results_to_file
#from .utils.bigquery_utils import fetch_data_from_bigquery
from .config.constants import DEFAULT_EXEC_DATE, OUTPUT_FILE_PATH
from .validators.result_validator import validate_result

logger = get_logger(__name__)

@task
def fetch_data_task(query):
    return fetch_data_from_bigquery(query)

@task
def preprocess_task(raw_data):
    return preprocess(raw_data)

@task
def train_task(data):
    return train(data)

@task
def infer_task(model):
    return infer(model)

@task
def validate_task(results):
    validate_result(results)

@task
def save_results_task(results, OUTPUT_FILE_PATH):
    save_results_to_file(results, OUTPUT_FILE_PATH)

@flow
def ml_pipeline(exec_date: str, test_data: pd.DataFrame = None) -> None:
    try:
        logger.info(f"ML Pipeline started with exec_date: {exec_date}")
        
        if test_data is None:
            # BigQueryからデータを取得
            query = "SELECT * FROM your_table WHERE date = @exec_date"
            # raw_data = fetch_data_from_bigquery(query)
            raw_data = pd.DataFrame({'result': ['success'], 'value': [1]})
        else:
            logger.info("Using provided test data.")
            raw_data = test_data
        
        # データの前処理
        processed_data = preprocess_task(raw_data)
        
        # モデルのトレーニング
        model = train_task(processed_data)
        
        # 推論
        results = infer_task(model)
        
        # 結果のバリデーション
        validate_task(results)
        
        # 結果をファイルに保存
        save_results_task(results, OUTPUT_FILE_PATH)
        
        # 結果をBigtableに保存
        # save_to_bigtable(results)
        
        logger.info("ML Pipeline completed successfully.")
    except Exception as e:
        logger.error(f"ML Pipeline failed: {e}")
        raise

def main():
    parser = argparse.ArgumentParser(description="Run the ML pipeline.")
    parser.add_argument("--exec_date", type=str, default=DEFAULT_EXEC_DATE, help="Execution date for the pipeline.")
    args = parser.parse_args()

    ml_pipeline(exec_date=args.exec_date)

if __name__ == "__main__":
    main()