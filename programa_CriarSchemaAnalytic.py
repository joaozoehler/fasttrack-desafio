# Programa elaborado para o desafio final da Fast track em Data & Analytics ed. 2021-09
# Executado inicialmente em computador com Windows 10
import mysql.connector as msql
from mysql.connector import Error

# Definição das variáveis do bd
nome_schema = 'analytic'

# Tentativa de conexão no banco e criação do schema
try:
    conexao = msql.connect(host='localhost', port='3306', user='admin', password='admin')
    if conexao.is_connected():
        cursor = conexao.cursor()
        cursor.execute(f"CREATE DATABASE {nome_schema}")
        print("O banco de dados foi criado com sucesso.")
except Error as e:
    print("Error while connecting to MySQL", e)

# Conexão no banco e schema
conexao = msql.connect(host='localhost', port='3306', database=nome_schema, user='admin', password='admin')
if conexao.is_connected():
    cursor = conexao.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    print(f"Sua conexão ao banco {record} foi estabelecida")

    cursor.execute('CREATE TABLE fact_merchant_kpi\
                    SELECT\
                    CONCAT(t.ano,"-", t.mes,"-", t.dia) AS data,\
                    t.merchant,\
                    SUM(t.amount) AS TPV,\
                    COUNT(DISTINCT t.id) AS qtd_transacoes\
                    FROM desafio_pagseguro.transactions AS t\
                    GROUP BY t.merchant\
                    ORDER BY t.merchant')

    cursor.execute('CREATE TABLE fact_customer_kpi\
                    SELECT\
                    CONCAT (t.ano, "-", t.mes, "-", t.ano) AS data,\
                    t.merchant,\
                    t.customer,\
                    SUM(t.amount) AS TPV,\
                    COUNT(DISTINCT t.id) AS qtd_transacoes\
                    FROM desafio_pagseguro.transactions AS t\
                    GROUP BY t.customer\
                    ORDER BY CONCAT(t.ano, "-", t.mes, "-", t.ano)')

    cursor.execute('CREATE TABLE dim_merchant_category\
                    SELECT\
                    t.merchant, t.category\
                    FROM desafio_pagseguro.transactions AS t\
                    GROUP BY t.merchant\
                    ORDER BY t.category')

conexao.commit()