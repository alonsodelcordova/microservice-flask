from flask import Flask, request, jsonify

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 1200},
    {"id": 2, "name": "Mouse", "price": 20}
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return jsonify(product), 200
    return jsonify({"error": "Product not found"}), 404

@app.route('/products', methods=['POST'])
def add_product():
    data = request.json
    new_product = {"id": len(products) + 1, **data}
    products.append(new_product)
    return jsonify(new_product), 201

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.json
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        product.update(data)
        return jsonify(product), 200
    return jsonify({"error": "Product not found"}), 404

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    products = [p for p in products if p["id"] != product_id]
    return jsonify({"message": "Product deleted"}), 200

if __name__ == '__main__':
    app.run(port=5002)
