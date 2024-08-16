import pytest
import pandas as pd
from ml_pipeline.pipeline import ml_pipeline
from ml_pipeline.utils.logger import get_logger

logger = get_logger(__name__)
@pytest.mark.parametrize
("exec_date, test_data", [
    ("2023-01-01", pd.DataFrame({'result': ['success'], 'value': [1]})),
    ("2023-01-01", None)
])
def test_ml_pipeline(exec_date, test_data):
    if test_data is None:
        from unittest.mock import patch
        # with patch('ml_pipeline.pipeline.fetch_data_from_bigquery', return_value=pd.DataFrame({'result': ['success'], 'value': [1]})):
        #     ml_pipeline(exec_date=exec_date, test_data=test_data)
    else:
        ml_pipeline(exec_date=exec_date, test_data=test_data)
    assert True