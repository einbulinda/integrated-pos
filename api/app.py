from flask import Flask
from flask_cors import CORS
from flask_restx import Api
from core.config import settings
from modules.auth.routes import api as auth_ns
from modules.catalogue.routes import api as catalogue_ns
from modules.cart.routes import api as cart_ns
from modules.orders.routes import api as orders_ns
from modules.payments.routes import api as payments_ns


def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True, resources={
         r"*": {"origins": settings.CORS_ORIGINS}})

    api = Api(app, version="1.0.0", title="Integrated POS API",
              description="eCommerce + POS API", doc="/docs")  # Swagger UI

    api.add_namespace(auth_ns, path="/api/auth")
    api.add_namespace(catalogue_ns, path="/api/catalogue")
    api.add_namespace(cart_ns, path="/api/cart")
    api.add_namespace(orders_ns, path="/api/orders")
    api.add_namespace(payments_ns, path="/api/payments")

    return app


app = create_app()

if __name__ == "__main__":
    app.run(port=settings.APP_PORT, debug=True)
