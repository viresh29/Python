from datetime import datetime

from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021, 2, 1, 7, 0).isoformat(),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0
}


def test_callable(msg, *args, **kwargs):
    return msg


def create_dag():
    with DAG(dag_id='test_dag', default_args=default_args, schedule_interval='@daily') as dag:
        test_task = PythonOperator(task_id='test_task',
                                   python_callable=test_callable,
                                   op_kwargs={
                                       'msg': 'Hello Airflow!!'
                                   },
                                   provide_context=True,
                                   retries=0
                                   )

        test_task

    return dag


globals()['test_dag'] = create_dag()
