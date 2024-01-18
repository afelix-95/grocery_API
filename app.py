# app.py

from flask import render_template
import config
from models import Product

app = config.connex_app
app.add_api(config.basedir / "swagger.yml")

@app.route("/")
def home():
    products = Product.query.all()
    return render_template("home.html", products=products)

if __name__ == "__main__":
    app.run()