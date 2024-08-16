from google.cloud import bigquery
import pandas as pd

def fetch_data_from_bigquery(query: str) -> pd.DataFrame:
    client = bigquery.Client()
    query_job = client.query(query)
    return query_job.to_dataframe()