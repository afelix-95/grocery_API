# products.py

from flask import abort, make_response

from config import db
from models import Product, product_schema, products_schema

def read_all():
    products = Product.query.all()
    return products_schema.dump(products)

def create(product):
    name = product.get("name")
    existing_product = Product.query.filter(Product.name == name).one_or_none()

    if existing_product is None:
        new_product = product_schema.load(product, session=db.session)
        db.session.add(new_product)
        db.session.commit()
        return product_schema.dump(new_product), 201
    else:
        abort(406, f"Product {name} already exists")

def read_one(name):
    product = Product.query.filter(Product.name == name).one_or_none()

    if product is not None:
        return product_schema.dump(product)
    else:
        abort(404, f"Product with name {name} not found")

def update(name, product):
    existing_product = Product.query.filter(Product.name == name).one_or_none()

    if existing_product:
        update_product = product_schema.load(product, session=db.session)
        existing_product.category = update_product.category
        existing_product.quantity = update_product.quantity
        existing_product.price = update_product.price
        db.session.merge(existing_product)
        db.session.commit()
        return product_schema.dump(existing_product), 201
    else:
        abort(404, f"Product with name {name} not found")

def delete(name):
    existing_product = Product.query.filter(Product.name == name).one_or_none()

    if existing_product:
        db.session.delete(existing_product)
        db.session.commit()
        return make_response(f"{name} successfully deleted", 200)
    else:
        abort(404, f"Product with name {name} not found")