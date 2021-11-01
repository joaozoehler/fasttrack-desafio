import mysql.connector as msql
from mysql.connector import Error

# Definição das variáveis do bd
nome_schema = 'desafio_pagseguro'
nome_tabela = 'transactions'

# Tentativa de conexão no banco e criação do schema
try:
    conexao = msql.connect(host='localhost', port='3306', user='admin', password='viale1721')
    if conexao.is_connected():
        cursor = conexao.cursor()
        cursor.execute("SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''))")
        cursor.execute("SET SESSION sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''))")
        cursor.execute(f"CREATE DATABASE {nome_schema}")
        print("O banco de dados foi criado com sucesso.")
        conexao.commit()
except Error as e:
    print("Error while connecting to MySQL", e)