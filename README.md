# grocery_API
 An API that handles HTTP requests for a supermarket. It can be used, for example, by any delivery app that wants to offer this supermarket's products as part of its deliverables.
## Instructions
This application defines the API endpoint `/products` to manage the list of available products in a supermarket. It handles requests for all the CRUD operations.
You can try out this application by installing `flask`, `flask_sqlalchemy`, `flask_marshmallow` and `connexion` with `pip`:
```
# Best practice, use a virtual environment rather than install in the base env
python -m venv venv
.venv\Scripts\activate
# The actual install command
pip install flask flask_sqlalchemy flask_marshmallow connexion
```
Then, you run `app.py` and a landing page in localhost:8000 will become available. This landing page allows you to perform any CRUD operations to the data stored in `product.db`.
The REST API documentation is also accessible through `http://localhost:8000/api/ui` or through the link in the landing page.
