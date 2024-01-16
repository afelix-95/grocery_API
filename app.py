from flask import Flask, request, jsonify

app = Flask(__name__)

products = [
    {"id": 100, "name": "Banana", "category": "Fruits", "quantity": 120, "price": 2.99},
    {"id": 101, "name": "Cod", "category": "Fish", "quantity": 200, "price": 5.99},
    {"id": 102, "name": "Bleach", "category": "Cleaning", "quantity": 510, "price": 10.00},
    {"id": 103, "name": "Frying pan", "category": "Cookware", "quantity": 70, "price": 45.99},
    {"id": 104, "name": "Water", "category": "Drinks", "quantity": 1120, "price": 1.99}
]

def _find_next_id():
    return max(product["id"] for product in products) + 1

@app.get("/products")
def get_products():
    return jsonify(products)

@app.post("/products")
def add_product():
    if request.is_json:
        product = request.get_json()
        product["id"] = _find_next_id()
        products.append(product)
        return product, 201
    return {"error": "Request must be JSON"}, 415

@app.get("/products/<int:product_id>")
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return product
    return {"error": "Product not found"}, 404

@app.put("/products/<int:product_id>")
def update_product(product_id):
    if request.is_json:
        product = next((p for p in products if p["id"] == product_id), None)
        if product:
            product.update(request.get_json())
            return product
        return {"error": "Product not found"}, 404
    return {"error": "Request must be JSON"}, 415

@app.delete("/products/<int:product_id>")
def delete_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        products.remove(product)
        return {"message": "Product removed"}, 200
    return {"error": "Product not found"}, 404