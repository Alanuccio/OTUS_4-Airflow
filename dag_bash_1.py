from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago

args = {
    'owner': 'airflow',
}

start_date_val = datetime.now() - timedelta(minutes=10)

dag = DAG(
    dag_id='airflow_homework_1',
    default_args=args,
    schedule_interval='*/5 * * * *',
    start_date=start_date_val,
    dagrun_timeout=timedelta(minutes=10),
    tags=['homework', 'Mmigutin'],
)

start_task = DummyOperator(
    task_id='start',
    dag=dag,
)

bash_path = '/home/airflow/plugins/getBitcoinInfo.sh'
run_this = BashOperator(
    task_id='own_bash_script',
    bash_command=f'. {bash_path} ',
    dag=dag,
)

end_task = DummyOperator(
    task_id='end',
    dag=dag
)

start_task >> run_this >> end_task

if __name__ == "__main__":
    dag.cli()
# End
