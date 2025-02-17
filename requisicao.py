# b) Crie um arquivo chamado requisicao.py e faça a requisição do seu endpoint utilizando a biblioteca requests! 

import requests


# endpoit criado no aqrquivo Fastapi
url_criada = "http://127.0.0.1:8000/"

requisicao = requests.get(url_criada)  # fazendo a requisição

# Condicional para confirmar o sucesso ou erro da requisição
if requisicao.status_code == 200:
  print(f"Requisição feita com sucesso. Resposta: {requisicao.json()}")
  
else:
  print(f"Falha na requisição. Status: {requisicao.status_code}")