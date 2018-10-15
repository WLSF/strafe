from flask import Flask
from api.src.db import setup_db
from api.src.routes import setup_routes


def create_app():
    app = Flask(__name__)

    app.config.from_object('api.settings.Config')

    setup_db(app)
    setup_routes(app)

    return app


app = create_app()
