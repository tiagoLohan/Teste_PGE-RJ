'''
Crie um endpoint utilizando a fastapi:
a) O objetivo é criar um endpoint que irá retornar um “Olá, mundo”.
b) Crie um arquivo chamado requisicao.py e faça a requisição do seu endpoint utilizando a biblioteca requests! 

'''


from fastapi import FastAPI

# a) O objetivo é criar um endpoint que irá retornar um “Olá, mundo”.

app = FastAPI()  #Criando a instância

# Rota com o retorno solicitado
@app.get("/")
def home():
  return "Olá, mundo"




