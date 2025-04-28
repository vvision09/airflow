from airflow import DAG
import datetime 
import pendulum #datetime 쉽게 사용하기 위한 라이브러리
from airflow.operators.bash import BashOperator 

# python 파일명과 상관없이 화면에서는 dag_id를 보여준다 (일반적으로 파일명과 일치시킴)
with DAG(
    dag_id = 'dags_bash_operator',
    schedule = '0 0 * * *', #분 시 일 월 요일
    start_date = pendulum.datetime(2025,4,28, tz='Asia/Seoul'),
    catchup = False # 일반적으로 False
    #tags=['bash'] # UI에서 태그만 눌렀을때 보는 용도
    #params = {} # 공통으로 넘길 파라미터
) as dag : 
    bash_t1 = BashOperator(
        task_id = 'bash_t1' # 객체명과 task id는 일치하는게 좋다
        ,bash_command = 'echo whoami'
    )

    bash_t2 = BashOperator(
        task_id = 'bash_t1' # 객체명과 task id는 일치하는게 좋다
        ,bash_command = 'echo $HOSTNAME'
    )

    bash_t1 >> bash_t2

