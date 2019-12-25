from flask import Flask
from routes.routes import routes as rota

def create_app():
    app = Flask(__name__)
    app.register_blueprint(rota)
    return app

