import pytest
import pandas as pd
from ml_pipeline.pipeline import ml_pipeline
from ml_pipeline.utils.logger import get_logger

logger = get_logger(__name__)

def test_ml_pipeline_with_test_data():
    test_data = pd.DataFrame({'result': ['success'], 'value': [1]})
    try:
        ml_pipeline(exec_date="2023-01-01", test_data=test_data)
        assert True
    except Exception as e:
        logger.error(f"Test failed: {e}")
        assert False

# def test_ml_pipeline_without_test_data(mocker):
#     mocker.patch('ml_pipeline.pipeline.fetch_data_from_bigquery', return_value=pd.DataFrame({'result': ['success'], 'value': [1]}))
#     try:
#         ml_pipeline(exec_date="2023-01-01")
#         assert True
#     except Exception as e:
#         logger.error(f"Test failed: {e}")
#         assert False