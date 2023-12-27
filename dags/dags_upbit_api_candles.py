from operators.upbit_api_to_csv_operator import UpbitApiToCsvOperator
from airflow import DAG
import pendulum

with DAG(
    dag_id='dags_upbit_api_candles',
    schedule='0 7 * * *',
    start_date=pendulum.datetime(2023,12,1, tz='Asia/Seoul'),
    catchup=False
) as dag:
    t1 = UpbitApiToCsvOperator(
        task_id='t1'
    )

    t1