from flask import Flask, request, jsonify

app = Flask(__name__)

sales = []

@app.route('/sales', methods=['GET'])
def get_sales():
    return jsonify(sales)

@app.route('/sales', methods=['POST'])
def record_sale():
    data = request.json
    sales.append(data)
    return jsonify({"message": "Sale recorded"}), 201

if __name__ == '__main__':
    app.run(port=5003)