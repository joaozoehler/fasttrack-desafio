import mysql.connector as msql
from mysql.connector import Error
import pandas as pd

# Definição das variáveis do bd
nome_schema = 'desafio_pagseguro'
nome_tabela = 'transactions'

pasta = '../dataset_from_kaggle'
arquivo = (f'{pasta}/bs140513_032310.csv')
dataset = pd.read_csv(f'{arquivo}', delimiter = ',', quotechar = "'", index_col = False)

# Conexão no banco e schema
conexao = msql.connect(host='localhost', port='3306', database=nome_schema, user='admin', password='viale1721')
if conexao.is_connected():
    cursor = conexao.cursor()
    cursor.execute("SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''))")
    cursor.execute("SET SESSION sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''))")
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

# Adiciona coluna "id" (INT) com incrementação automática
    cursor.execute(f"ALTER TABLE {nome_tabela} ADD id INT NOT NULL PRIMARY KEY AUTO_INCREMENT FIRST")

# Adiciona a coluna "ano" com o valor "2021" (SMALLINT) default
    cursor.execute(f"ALTER TABLE {nome_tabela} ADD ano SMALLINT DEFAULT 2021")

# Adiciona a coluna "mes" sem valor com o type (SMALLINT)
    cursor.execute(f"ALTER TABLE {nome_tabela} ADD mes SMALLINT")

# Adiciona a coluna "dia" com o valor "1" (SMALLINT) default
    cursor.execute(f"ALTER TABLE {nome_tabela} ADD dia SMALLINT DEFAULT 1")

# Adiciona os valores na coluna "mes" conforme dados da coluna "step"
    cursor.execute(f"UPDATE {nome_tabela}\
	                SET mes = CASE\
                    WHEN (step < 31) THEN 1\
                    WHEN (step > 30) AND (step < 61) THEN 2\
                    WHEN (step > 60) AND (step < 91) THEN 3\
                    WHEN (step > 90) AND (step < 121) THEN 4\
                    WHEN (step > 120) AND (step < 151) THEN 5\
                    WHEN (step > 150) AND (step < 181) THEN 6\
                    END")

# Adiciona a coluna "data" via concatenação
    cursor.execute(f"ALTER TABLE {nome_tabela}\
                    ADD data VARCHAR(255)\
                        DEFAULT (CONCAT(ano, '-', mes, '-', '1'))")

# Deixar NULL onde coluna "amount" for 0 (zero)
cursor.execute(f"UPDATE {nome_tabela}\
                SET amount = NULL WHERE amount = 0")

cursor.execute(f"UPDATE {nome_tabela}\
                SET age = NULL WHERE age = 'U'")

cursor.execute(f"UPDATE {nome_tabela}\
                SET gender = NULL WHERE gender = 'U'")

cursor.execute(f"UPDATE {nome_tabela}\
                SET gender = NULL WHERE gender = 'E'")

conexao.commit()