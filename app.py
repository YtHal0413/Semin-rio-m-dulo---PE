from flask import Flask, jsonify

# Cria a aplicação Flask
app = Flask(__name__)   

# Cria uma rota inicial com texto simples
@app.route("/")
def home():
    return "Bem-vindo ao Flask com jsonify!"

# Cria uma rota URL secundária de API com JSON
@app.route("/api/products")
def products():
    data = [
        {"id": 1, "name": "Notebook", "price": 6900},
        {"id": 2, "name": "Mouse", "price": 15},
        {"id": 3, "name": "Teclado", "price": 50}
    ]
    # Converte para JSON
    return jsonify(data)  
# Inicia servidor local
if __name__ == "__main__":
    app.run(debug=True)   