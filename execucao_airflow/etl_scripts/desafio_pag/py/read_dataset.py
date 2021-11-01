import pandas as pd

## Horário da pasta
pasta = '../dataset_from_kaggle'

# Definição das variáveis do dataset a ser lido
arquivo = (f'{pasta}/bs140513_032310.csv')
dataset = pd.read_csv(f'{arquivo}', delimiter = ',', quotechar = "'", index_col = False)