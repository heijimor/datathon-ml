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
            'output_path': '/shared-artifacts/artifacts/notebooks/perform_users.ipynb'
        }
    )

    perform_articles_task = PythonOperator(
        task_id='perform_articles',
        python_callable=execute_notebook,
        op_kwargs={
            'input_path': '/usr/local/airflow/pipeline/perform_articles.ipynb',
            'output_path': '/shared-artifacts/artifacts/notebooks/perform_articles.ipynb'
        }
    )

    pre_processing_users_task = PythonOperator(
        task_id='pre_processing_users',
        python_callable=execute_notebook,
        op_kwargs={
            'input_path': '/usr/local/airflow/pipeline/pre_processing_users.ipynb',
            'output_path': '/shared-artifacts/artifacts/notebooks/pre_processing_users.ipynb'
        }
    )
    
    pre_processing_articles_task = PythonOperator(
        task_id='pre_processing_articles',
        python_callable=execute_notebook,
        op_kwargs={
            'input_path': '/usr/local/airflow/pipeline/pre_processing_articles.ipynb',
            'output_path': '/shared-artifacts/artifacts/notebooks/pre_processing_articles.ipynb'
        }
    )

    train_model = PythonOperator(
        task_id='train_model',
        python_callable=execute_notebook,
        op_kwargs={
            'input_path': '/usr/local/airflow/pipeline/train_model.ipynb',
            'output_path': '/shared-artifacts/artifacts/notebooks/train_model.ipynb'
        }
    )

    pre_processing_validacao_task = PythonOperator(
        task_id='pre_processing_validacao',
        python_callable=execute_notebook,
        op_kwargs={
            'input_path': '/usr/local/airflow/pipeline/pre_processing_validacao.ipynb',
            'output_path': '/shared-artifacts/artifacts/notebooks/pre_processing_validacao.ipynb'
        }
    )
    
    evaluate_task = PythonOperator(
        task_id='evaluate',
        python_callable=execute_notebook,
        op_kwargs={
            'input_path': '/usr/local/airflow/pipeline/evaluate.ipynb',
            'output_path': '/shared-artifacts/artifacts/notebooks/evaluate.ipynb'
        }
    )

    perform_users_task >> perform_articles_task >> pre_processing_users_task >> pre_processing_articles_task >> train_model >> pre_processing_validacao_task >> evaluate_task