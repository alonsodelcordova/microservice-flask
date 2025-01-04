from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

PATH_URL = "http://127.0.0.1"

# Mapeo dinámico de microservicios
SERVICES = {
    "auth": PATH_URL + ":5001",
    "products": PATH_URL + ":5002",
    "sales": PATH_URL + ":5003",
    "warehouse": PATH_URL + ":5004",
}

@app.route('/<service>/<path:subpath>', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def proxy(service, subpath):

    # obtener ID del cliente
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = request.headers.get('User-Agent', 'Unknown')
    print(f"Cliente: {client_ip}, User-Agent: {user_agent}")
    

    if service not in SERVICES:
        return jsonify({"error": "Service not found"}), 404

    url = f"{SERVICES[service]}/{subpath}"  # Construye la URL del microservicio
    method = request.method
    print("ir a : "+url)
    print("metodo : "+method)
    # Construye los encabezados; usa los que vienen de la solicitud original
    headers = {
        key: value for key, value in request.headers if key != 'Host'
    }

    # Realiza la solicitud al microservicio correspondiente
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            json=request.get_json(silent=True),  # Cuerpo de la solicitud en JSON
            params=request.args  # Parámetros de consulta (query params)
        )

        # Retorna la respuesta del microservicio, incluyendo el contenido y el código de estado
        return (response.content, response.status_code, response.headers.items())

    except requests.exceptions.RequestException as e:
        # Maneja cualquier error que ocurra durante la solicitud
        return jsonify({"error": "Failed to connect to service", "details": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
