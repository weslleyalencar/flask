from flask import Flask, json
import requests 
app = Flask(__name__)

@app.route('/<cep>')
def home(cep):
    dados = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    return json.loads(dados.content)
