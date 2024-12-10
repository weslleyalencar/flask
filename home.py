from flask import Flask, json
import requests 
import api
app = Flask(__name__)

@app.route('/<cep>')
def home(cep):
    dados = api.get_cep(cep)
    return dados

if __name__ == "__main__":
    app.run(debug=True)