
# Project with the FIPE API
# First of all, the user have to make some INPUT so we can to seatch at FIPE API
# Data flow have been sent to a PBI aplication in simple views and GPT texts interpretations
# All this will be present by a smartphone APP 

# STEPS 
# 1- Conect to FIPE API
# 2- Learn the right inputs to api
# 3 - Develop a smart dashboard integrated with GPT CHAT 
# 4 - Develop a smarthphone app to show it


# https://deividfortuna.github.io/fipe/v2/#operation/GetFipeInfo
# Busca histórico de alimentação da API
import requests
url = "https://parallelum.com.br/fipe/api/v2/references"
response = requests.get(url, verify=False)
if response.status_code == 200:
    data = response.json()
    for item in data:
        print("Code:", item["code"])
        print("Month:", item["month"])
else:
    print("Falha ao obter os dados:", response.status_code)


# DF COM MARCAS
import pandas as pd
def obter_marcas(vehicle_type):
    url = f"https://parallelum.com.br/fipe/api/v2/{vehicle_type}/brands"
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Erro ao obter marcas da API da FIPE.")
        return None

marcas = obter_marcas(vehicle_type)
df = pd.DataFrame(marcas)
print(df)






# DF COM MARCAS E MODELOS
import requests
import pandas as pd
def obter_dados_por_marca(vehicle_type, brand_id):
    url = f"https://parallelum.com.br/fipe/api/v2/{vehicle_type}/brands/{brand_id}/models"
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Erro ao obter dados da API da FIPE.")
        return None

vehicle_type = 'cars'
brand_id = '5' 
dados_marca = obter_dados_por_marca(vehicle_type, brand_id)
df_marca = pd.DataFrame(dados_marca)
print(df_marca)






# DF COM MARCAS, MODELOS E ANO
def obter_dados_por_ano(vehicle_type, brand_id, model_id):
    url = f"https://parallelum.com.br/fipe/api/v2/{vehicle_type}/brands/{brand_id}/models/{model_id}/years"
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Erro ao obter dados da API da FIPE.")
        return None

vehicle_type = 'cars'
brand_id = '5'
model_id = '42'

dados_ano = obter_dados_por_ano(vehicle_type, brand_id, model_id)
df_ano = pd.DataFrame(dados_ano)
print(df_ano)







# OBTEM FIPE CODE
def obter_dados_por_ano(vehicle_type, brand_id, model_id, year_id):
    url = f"https://parallelum.com.br/fipe/api/v2/{vehicle_type}/brands/{brand_id}/models/{model_id}/years/{year_id}/"
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Erro ao obter dados da API da FIPE.")
        return None


vehicle_type = 'cars'
brand_id = '57'
model_id = '5652'
year_id = '2012-2'
#! ERRO
dados_ano = obter_dados_por_ano(vehicle_type, brand_id, model_id, year_id)
df_ano = pd.DataFrame(dados_ano)




















# TST preços
def obter_historico_preco(vehicle_type, fipe_code, year_id):
    url = f"https://parallelum.com.br/fipe/api/v2/{vehicle_type}/{fipe_code}/years/{year_id}/history"
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Erro ao obter histórico de preços da API da FIPE.")
        return None

# Substitua 'fipe_code' e 'year_id' pelos valores desejados
fipe_code = '004278-1'
year_id = '2005-1'
historico_preco = obter_historico_preco(vehicle_type, fipe_code, year_id)
df_historico = pd.DataFrame(historico_preco)
print(df_historico)
