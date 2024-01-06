from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
import datetime
import pendulum

with DAG(
   dag_id="dags_bash_operator", # airflow 처음 들어왔을 때 화면에서 보이는 DAG 이름(파이썬 파일명이랑 상관없음), 일반적으로  파일명과 일치시켜주는 것이 좋음 
   schedule="0 0 * * *", # cron (분 시 일 월 요일)
   start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
   catchup=False, # start_date와 같이, 현재가 3월 1일일때 1월 1일 부터 3월 1일까지의 데이터를 돌릴 것인지 설정 (기본적으로 False로 설정)
   #dagrun_timeout=datetime.timedelta(minutes=60), # DAG이 60분 이상 돌면 실패하도록 설정
   #tags=["example", "example2"], # 화면에서 파란색 박스, 태그를 눌렀을 때 카테고리화 해서 볼 수 있음
   #params={"example_key": "example_value"}, # DAG밑에 TASK를 둘건데 Task에 공통적으로 넘겨줄 파라미터 
) as dag: # task
   bash_t1 = run_this = BashOperator(  # task 명 = 
       task_id="bash_t1", # task 명도 객체명과 동일하게 주는것이 좋다. 
       bash_command="echo whoami", # whami 스트링 출력
    )
   bash_t2 = run_this = BashOperator(  # task 명 = 
       task_id="bash_t2", # task 명도 객체명과 동일하게 주는것이 좋다. 
       bash_command="echo $HOSTNAME", # whami 스트링 출력
    )
   bash_t1 >> bash_t2