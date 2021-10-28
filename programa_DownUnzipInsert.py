# Programa elaborado para o desafio final da Fast track em Data & Analytics ed. 2021-09
# Executado inicialmente em computador com Windows 10
import kaggle
import zipfile
import pandas as pd
import mysql.connector as msql
import mysql.connector
from mysql.connector import Error

# Download do dataset via Kaggle API
# O download só funciona com o arquivo "kaggle.json" inserido em C:\Users\<usuário>\.kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi ()
api.authenticate()
api.dataset_download_file('ealaxi/banksim1', file_name = 'bs140513_032310.csv')

# Descompatação do dataset
with zipfile.ZipFile('bs140513_032310.csv.zip', 'r') as zipref:
    zipref.extractall()

# Definição das variáveis do bd
nome_schema = 'desafio_pagseguro'
nome_tabela = 'transactions'

# Definição das variáveis do dataset a ser lido
arquivo = 'bs140513_032310.csv'
dataset = pd.read_csv(f'{arquivo}', delimiter = ',', quotechar = "'", index_col = False)

# Tentativa de conexão no banco e criação do schema
try:
    conn = msql.connect(host='localhost', port='3306', user='admin', password='admin')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE {nome_schema}")
        print("O banco de dados foi criado com sucesso.")
except Error as e:
    print("Error while connecting to MySQL", e)

# Conexão no banco e schema
conn = mysql.connector.connect(host='localhost', port='3306', database=nome_schema, user='admin', password='admin')
if conn.is_connected():
    cursor = conn.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    print(f"Sua conexão ao banco {record} foi estabelecida")

    cursor.execute(f'DROP TABLE IF EXISTS {nome_tabela};')
    print('Criando a tabela...')

    cursor.execute(f"CREATE TABLE {nome_tabela}(step varchar(255),\
                                                customer varchar(255),\
                                                age varchar(255),\
                                                gender varchar(255),\
                                                zipcodeOri varchar(255),\
                                                merchant varchar(255),\
                                                zipMerchant varchar(255),\
                                                category varchar(255),\
                                                amount varchar(255),\
                                                fraud varchar(255))")
    print("A tabela foi criada...")

# Itera no dataset e a cada linha insere no banco
    for i,row in dataset.iterrows():
        sql = (f"INSERT INTO {nome_schema}.{nome_tabela} VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        cursor.execute(sql, tuple(row))
        print(f"Dado inserido")

# Adiciona coluna "id" com incrementação automática
    cursor.execute(f"ALTER TABLE {nome_tabela} ADD id INT NOT NULL PRIMARY KEY AUTO_INCREMENT FIRST")
conn.commit()