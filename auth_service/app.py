from flask import Flask, request, jsonify
import uuid
app = Flask(__name__)

users = {"admin": "123"}  # Usuarios de prueba

token = uuid.uuid4()  # Token de autenticación

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if users.get(username) == password:
        return jsonify({"message": "Login successful", "token": token}), 200
    return jsonify({"error": "Invalid credentials"}), 401

@app.get('/')
def dataGet():
    return jsonify({"message": "Base"}), 200

if __name__ == '__main__':
    app.run(port=5001, debug=True)