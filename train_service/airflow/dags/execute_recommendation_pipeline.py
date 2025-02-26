from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import papermill as pm

def execute_notebook(input_path, output_path):
    pm.execute_notebook(input_path, output_path)

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 2, 25),
    'retries': 1,
}

with DAG(
    'execute_recommendation_pipeline',
    default_args=default_args,
    schedule_interval=None,
    catchup=False
) as dag:
    perform_users_task = PythonOperator(
        task_id='perform_users',
        python_callable=execute_notebook,
        op_kwargs={
            'input_path': '/usr/local/airflow/pipeline/perform_users.ipynb',
            'output_path': '/usr/local/airflow/artifacts/notebooks/perform_users.ipynb'
        }
    )

    perform_articles_task = PythonOperator(
        task_id='perform_articles',
        python_callable=execute_notebook,
        op_kwargs={
            'input_path': '/usr/local/airflow/pipeline/perform_articles.ipynb',
            'output_path': '/usr/local/airflow/artifacts/notebooks/perform_articles.ipynb'
        }
    )

    pre_processing_task = PythonOperator(
        task_id='pre_processing',
        python_callable=execute_notebook,
        op_kwargs={
            'input_path': '/usr/local/airflow/pipeline/pre_processing.ipynb',
            'output_path': '/usr/local/airflow/artifacts/notebooks/pre_processing.ipynb'
        }
    )

    train_model_task = PythonOperator(
        task_id='train_model',
        python_callable=execute_notebook,
        op_kwargs={
            'input_path': '/usr/local/airflow/pipeline/train.ipynb',
            'output_path': '/usr/local/airflow/artifacts/notebooks/train.ipynb'
        }
    )

    perform_users_task >> perform_articles_task >> pre_processing_task >> train_model_task
