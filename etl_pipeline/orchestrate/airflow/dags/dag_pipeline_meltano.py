from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'start_date': datetime(2024, 7, 11),
    'retries': 3,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG('meltano_pipeline', default_args=default_args, schedule_interval='@once')

meltano_extract_from_csv_load_csv_step_1 = BashOperator(
    task_id='extract_from_csv_load_csv_step_1',
    bash_command='meltano el tap-csv target-csv--order-details',
    dag=dag
)

meltano_extract_from_postgres_load_csv_step_1 = BashOperator(
    task_id='extract_from_postgres_load_csv_step_1',
    bash_command='meltano el tap-postgres target-csv',
    dag=dag
)

meltano_extract_from_csv_load_postgres_step_2 = BashOperator(
    task_id='extract_from_csv_load_postgres_step_2',
    bash_command='meltano el tap-csv--step-2 target-postgres',
    dag=dag
)




[meltano_extract_from_csv_load_csv_step_1, meltano_extract_from_postgres_load_csv_step_1] >> meltano_extract_from_csv_load_postgres_step_2