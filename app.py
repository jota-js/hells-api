from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para o endpoint /api
@app.route('/api')
def api():
    try:
        # Fazendo uma requisição para o YouTube
        response = requests.get('https://www.youtube.com')
        return jsonify({"data": response.text})  # Retornando o conteúdo da página
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Erro ao acessar o YouTube: {str(e)}"}), 500

# Iniciar o servidor
if __name__ == '__main__':
    app.run(debug=True)
