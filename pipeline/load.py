from google.cloud import bigquery

def load_data(df):

    client = bigquery.Client()

    table_id = "data-pipeline-prod.dataset1.iris"

    job = client.load_table_from_dataframe(df, table_id)

    job.result()

    print("Loaded to BigQuery")