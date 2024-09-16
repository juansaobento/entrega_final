import datetime as dt
from airflow import DAG
from airflow.operators.python import PythonOperator
import sys
sys.path.append('/opt/airflow/dags/modules')
from modules import llamado_api,conexion_RS,creacion_df,send_email
from datetime import datetime, timedelta
import requests 
import json
import pandas as pd
import psycopg2 
import sqlalchemy as sa
import os
from dotenv import load_dotenv


default_args={
    'owner': 'juansaobento',
    'email_on_failure': True,
    'email_on_retry': False,
    'retries':3,
    'retry_delay': timedelta(minutes=1)
}   

with DAG (
    default_args=default_args,
    dag_id="etl-cocktails",
    schedule="@daily",
    start_date=dt.datetime(year=2024, month=8, day=25),
    end_date=None,
    catchup=True,
    tags=["etl", "cocktails"],
    doc_md="Este dag permite extraer y cargar cocktails"
    ) as dag:
    
    api_call= PythonOperator(
            dag= dag,
            task_id="obtencion-operator",
            python_callable= llamado_api
            )
    
    df_builder= PythonOperator(
            dag= dag,
            task_id="creacion-data-frame",
            python_callable= creacion_df
            )
    
    rs_conection= PythonOperator(
            dag= dag,
            task_id="conexion-rs",
            python_callable= conexion_RS
            )
    
    mail_sender= PythonOperator(
            dag= dag,
            task_id="envio-email",
            python_callable= send_email
            )
    api_call>>df_builder>>rs_conection>>mail_sender