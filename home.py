from flask import Flask, jsonify
import requests 

app = Flask(__name__)

@app.route('/<cep>')
def home(cep):
    try:
        # Fazer a requisição para a API ViaCEP
        dados = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

        # Verificar se a requisição foi bem-sucedida
        if dados.status_code == 200:
            # Retornar os dados como JSON
            return jsonify(dados.json())
        else:
            # Retornar erro caso o CEP não seja encontrado
            return jsonify({"error": "CEP não encontrado"}), 404
    except Exception as e:
        # Retornar mensagem de erro genérico
        return jsonify({"error": str(e)}), 500
