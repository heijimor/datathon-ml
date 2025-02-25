from airflow import DAG
from airflow.providers.papermill.operators.papermill import PapermillOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 1, 1),
    'retries': 1,
}

dag = DAG(
    'execute_jupyter_notebook',
    default_args=default_args,
    description='A simple DAG to execute a Jupyter Notebook',
    schedule_interval='@daily',
    catchup=False,
)

run_notebook = PapermillOperator(
    task_id='run_notebook',
    input_nb='/usr/local/airflow/documentation/heuristics.ipynb',
    output_nb='/usr/local/airflow/documentation/to/heuristics.ipynb',
    parameters={"param1": "value1"},
    dag=dag,
)

run_notebook