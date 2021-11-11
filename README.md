# Este documento contém algumas informações importantes sobre o projeto listado neste repositório

## Desafio final da Fast Track em Data & Analytics #202109AWS

### Descrição dos arquivos na raiz do repositório
* programa_DownUnzipInsert.py = versão para execução local das tarefas: 1) download de um dataset do Kaggle, 2) unzip do arquivo baixado (reconhecido previamente), 3) leitura via Pandas, 4) carga em um banco de dados MySQL instalado localmente, 5) adição de coluna "id" incremental na tabela "transactions" criada no schema, 6) adição de colunas ano/mês/dia e contabilização de mês a partir da coluna "step" e, por fim, 7) substituição de valores em duas colunas ("age" e "gender")
* programa_CriarSchemaAnalytic.py = versão para execução local da criação de novo schema a partir da tabela "transactions" no banco criado anteriormente (denominado "desafio_pagseguro")
* conhecendo_dataset.ipynb = notebook criado via VScode para conhecimento dos dados registrados no dataset

## Descrição dos arquivos na pasta "execucao_airflow"
* programa_etl.py = programa com a DAG principal dessa atividade no Apache Airflow
* unzip.py = download e unzip do dataset oriundo do Kaggle
* sql.py = criação do schema "desafio_pagseguro" e da tabela "transactions"
* ingest_sql.py = ingestão de todas as linhas do dataset (CSV) para o bd MySQL
* analytic.py = criação do schema "analytic" e de três tabelas a partir da tabela "transactions" ("fact_merchant_kpi", "fact_customer_kpi" e "dim_merchant_category"

## Descrição dos arquivos na pasta "consultas_sql"
* Consultas .sql criadas via MySQL Workbench para testes prévios à ingestão (organização dos códigos) e posteriores (teste com o banco de dados criado localmente via Apache Airflow ou Python)

## Descrição dos arquivos na pasta "dataset"
* bs140513_032310.csv.zip = dataset zipado obtido via download do Kaggle
* bs140513_032310.csv = dataset mencionado acima, em sua versão descompactada
