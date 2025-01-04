from flask import Flask, request, jsonify

app = Flask(__name__)

users = {"admin": "123"}  # Usuarios de prueba

@app.route('/auth/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if users.get(username) == password:
        return jsonify({"message": "Login successful", "token": "fake-jwt-token"}), 200
    return jsonify({"error": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(port=5001)