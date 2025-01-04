from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

PATH_URL = "http://localhost"

# Mapeo dinámico de microservicios
SERVICES = {
    "auth": PATH_URL + ":5001",
    "products": PATH_URL + ":5002",
    "sales": PATH_URL + ":5003",
    "warehouse": PATH_URL + ":5004",
}

@app.route('/<service>/<path:subpath>', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def proxy(service, subpath):
    if service not in SERVICES:
        return jsonify({"error": "Service not found"}), 404

    url = f"{SERVICES[service]}/{subpath}"  # Construye la URL del microservicio
    method = request.method

    # Redirige la solicitud al microservicio correspondiente
    response = requests.request(
        method=method,
        url=url,
        headers=request.headers,
        json=request.json,
        params=request.args
    )

    # Retorna la respuesta del microservicio
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
