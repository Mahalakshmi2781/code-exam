from flask import Flask, jsonify, request, abort
from database import get_db_connection

app = Flask(__name__)

# GET /api/products - List all products (with optional pagination)
@app.route('/api/products', methods=['GET'])
def get_products():
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    offset = (page - 1) * limit

    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products LIMIT ? OFFSET ?', (limit, offset)).fetchall()
    conn.close()

    result = [dict(product) for product in products]
    return jsonify(result), 200

# GET /api/products/<id> - Get product by ID
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    conn = get_db_connection()
    product = conn.execute('SELECT * FROM products WHERE id = ?', (product_id,)).fetchone()
    conn.close()

    if product is None:
        return jsonify({'error': 'Product not found'}), 404

    return jsonify(dict(product)), 200

# Custom error handler for invalid routes
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
