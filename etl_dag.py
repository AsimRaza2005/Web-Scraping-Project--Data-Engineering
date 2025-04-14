from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import os

# Define task functions by importing your scripts
def run_scrape():
    os.system("python /airflow/dags/scrape.py")

def run_transform():
    os.system("python airflow/dags/transform.py")

def run_load():
    os.system("python airflow/dags/load.py")

# DAG definition
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1
}

with DAG(
    dag_id='lab_data_etl',
    default_args=default_args,
    description='ETL pipeline for lab data from Marham.pk',
    schedule_interval='@daily',  # run once a day
    catchup=False
) as dag:

    scrape_task = PythonOperator(
        task_id='scrape_data',
        python_callable=run_scrape
    )

    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=run_transform
    )

    load_task = PythonOperator(
        task_id='load_to_mysql',
        python_callable=run_load
    )

    # Task pipeline
    scrape_task >> transform_task >> load_task
