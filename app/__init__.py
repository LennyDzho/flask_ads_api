from flask import Flask
from app.routes.ad_routes import ad_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(ad_bp)
    return app
