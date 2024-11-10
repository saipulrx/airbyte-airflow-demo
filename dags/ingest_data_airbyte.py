from datetime import datetime
from airflow.decorators import dag
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator

@dag(
    start_date=datetime(2024,11,10),
    schedule='@daily',
    catchup=False,
    tags=['airbyte','airflow'],
)

def ingest_data_airbyte():
    csv_to_postgres = AirbyteTriggerSyncOperator(
        task_id='ingest_csv_to_postgres',
        airbyte_conn_id='airbyte_conn',
        connection_id='690a7f94-b28e-405d-b7ba-1c7658443557',
        asynchronous=False,
        timeout=3600,
        wait_seconds=3
    )

    csv_to_bigquery = AirbyteTriggerSyncOperator(
        task_id='ingest_csv_to_bigquery',
        airbyte_conn_id='airbyte_conn',
        connection_id='b9c7bfc2-2912-43d7-a82d-98817c106494',
        asynchronous=False,
        timeout=3600,
        wait_seconds=3
    )


    postgres_to_bigquery = AirbyteTriggerSyncOperator(
        task_id='ingest_postgres_to_bigquery',
        airbyte_conn_id='airbyte_conn',
        connection_id='2c765726-dcd9-4077-aaa0-07a8f165c5e2',
        asynchronous=False,
        timeout=3600,
        wait_seconds=3
    )

    csv_to_postgres >> csv_to_bigquery >> postgres_to_bigquery
    
ingest_data_airbyte()