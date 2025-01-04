from flask import Flask, request, jsonify

app = Flask(__name__)

warehouse_entries = []

@app.route('/warehouse', methods=['GET'])
def get_warehouse_entries():
    return jsonify(warehouse_entries)

@app.route('/warehouse', methods=['POST'])
def add_warehouse_entry():
    data = request.json
    warehouse_entries.append(data)
    return jsonify({"message": "Warehouse entry added"}), 201

if __name__ == '__main__':
    app.run(port=5004)