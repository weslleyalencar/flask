from flask import Flask
import api

app = Flask(__name__)

@app.route('/')
def home():
    return "Bem-vindo à API! Use /get_cep/<local> para buscar informações."

@app.route('/cep/<local>')
def get_cep(local):
    try:
        # Chama a função da API com o parâmetro recebido na URL
        dados = api.get_cep(local)
        return {"resultados": dados}
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == "__main__":
    app.run(debug=True)
