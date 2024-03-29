from airflow import DAG
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pendulum
import datetime
from email.mime.base import MIMEBase
from email import encoders
from airflow.operators.python import PythonOperator
import os

def send_email_with_attachment():
    msg = MIMEMultipart()
    msg['From'] = 'vision.io09o@gmail.com'
    msg['To'] = '보낼이메일@naver.com'
    msg['Subject'] = '[TEST] 제목'

    body = '내용'
    msg.attach(MIMEText(body, 'plain'))

    filename = '/opt/airflow/plugins/shell/test.txt'
    attachment = open(filename, 'rb')
    
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= " + os.path.basename(filename))

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('vision.io09o@gmail.com', 'ztuz gfpb lnfc mecb')
    text = msg.as_string()
    server.sendmail('vision.io09o@gmail.com', '이메일.com', text)
    server.quit()

with DAG(
    dag_id="dags_email_att_operator",
    schedule="0 8 1 * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    send_email_task = PythonOperator(
        task_id='send_email_task',
        python_callable=send_email_with_attachment
    )

    
