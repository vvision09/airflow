from airflow import DAG
import pendulum
import datetime
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id = "dags_conn_test",
    schedule=None,
    start_date = pendulum.datetime(2024,1,1,tz ="Asia/Seoul"),
    catchup=False
) as dag :  
    t1 = EmptyOperator( # 아무 기능을 수행하지 않는 오퍼레이터
        task_id = "t1" # 인수는 태스크 아이디 1개임
    )
    t2 = EmptyOperator(
        task_id = "t2"
    )
    t3 = EmptyOperator(
        task_id = "t3"
    )
    t4 = EmptyOperator(
        task_id = "t4"
    )
    t5 = EmptyOperator(
        task_id = "t5"
    )
    t6 = EmptyOperator(
        task_id = "t6"
    )
    t7 = EmptyOperator(
        task_id = "t7"
    )
    t8 = EmptyOperator(
        task_id = "t8"
    )

    t1 >> [t2,t3] >> t4
    t5 >> t4
    [t4,t7] >> t6 >> t8
