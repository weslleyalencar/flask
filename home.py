from flask import Flask, jsonify, json
import requests 
app = Flask(__name__)

@app.route('/endereco/<cep>')
def home(cep):
    dados = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    return json.loads(dados.content)

if __name__ == "__main__":
    app.run(debug=True)
