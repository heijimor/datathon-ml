from airflow import DAG
from airflow.providers.papermill.operators.papermill import PapermillOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 1, 1),
    'retries': 1,
}

dag = DAG(
    'execute_heuristics',
    default_args=default_args,
    description='A simple DAG to execute a some heuristics data',
    schedule_interval=None,
    catchup=False,
)

run_notebook = PapermillOperator(
    task_id='run_notebook',
    input_nb='/usr/local/airflow/documentation/heuristics.ipynb',
    output_nb='/usr/local/airflow/artifacts/notebooks/heuristics.ipynb',
    dag=dag,
)

run_notebook