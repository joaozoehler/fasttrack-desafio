# Importando as bibliotecas que vamos usar nesse exemplo
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator

# Definindo alguns argumentos básicos
default_args = {
   'owner': 'joaohzlemos',
   'depends_on_past': False,
   'start_date': datetime(2021, 10, 28),
   'retries': 0,
   }
# Nomeando a DAG e definindo quando ela vai ser executada (você pode usar argumentos em Crontab também caso queira que a DAG execute por exemplo todos os dias as 8 da manhã)
with DAG(
   'FastTrack_Desafio',
   schedule_interval = '@once',
   catchup = False,
   default_args = default_args
   ) as dag:
# Definindo as tarefas que a DAG vai executar, nesse caso a execução de dois programas Python, chamando sua execução por comandos bash
        t1 = BashOperator(
        task_id='DownloadDatasetKaggle',
        bash_command="""
        cd /home/airflow/dags/etl_scripts/desafio_pag/py/
        python3 unzip.py
        """)

      #   t2 = BashOperator(
      #   task_id='Read_downloaded_dataset_confirm',
      #   bash_command="""
      #   cd /home/airflow/dags/etl_scripts/desafio_pag/py/
      #   python3 read_dataset.py
      #   """)

        t3 = BashOperator(
        task_id='CriarSchemaNoMySQL',
        bash_command="""
        cd /home/airflow/dags/etl_scripts/desafio_pag/py/
        python3 sql.py
        """)

        t4 = BashOperator(
        task_id='InserirDadosDoCSVnoBancoMySQL',
        bash_command="""
        cd /home/airflow/dags/etl_scripts/desafio_pag/py/
        python3 ingest_sql.py
        """)

        t5 = BashOperator(
        task_id='CriarSchemaAnalyticNoMySQL',
        bash_command="""
        cd /home/airflow/dags/etl_scripts/desafio_pag/py/
        python3 analytic.py
        """)

# Definindo o padrão de execução, nesse caso executamos t1 e depois t2
t1 >> t3 >> t4 >> t5