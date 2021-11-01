import datetime
import kaggle
import zipfile

## Horário da pasta
pasta = '../dataset_from_kaggle'

# Download do dataset via Kaggle API
# O download só funciona com o arquivo "kaggle.json" inserido em C:\Users\<usuário>\.kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi ()
api.authenticate()
api.dataset_download_file('ealaxi/banksim1', file_name = 'bs140513_032310.csv', path = pasta)

# Descompatação do dataset
with zipfile.ZipFile(f'{pasta}/bs140513_032310.csv.zip', 'r') as zipref:
    zipref.extractall(pasta)