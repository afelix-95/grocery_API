#models.py

from config import db, ma

class Product(db.Model):
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    category = db.Column(db.String(32))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True
        sqla_session = db.session

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)