from flask import Flask, jsonify  # Importa a classe Flask e a função jsonify para retorno em JSON

app = Flask(__name__)  # Cria uma instância da aplicação Flask

@app.route("/")  # Define a rota raiz ("/")
def index():
    return "Hello from Flask Canary Deployment!"  # Retorna uma mensagem simples na raiz

@app.route("/health")  # Define uma rota de health check em "/health"
def health():
    return jsonify({"status": "ok"}), 200  # Retorna um JSON com status "ok" e HTTP 200

if __name__ == "__main__":  # Se o script for executado diretamente (e não importado como módulo)
    app.run(host="0.0.0.0", port=5000)  # Inicia o servidor Flask escutando em todas as interfaces na porta 5000
