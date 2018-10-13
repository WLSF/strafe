import os
import pytest
import tempfile

#from api.src.main import app
from api.src.sqlite import db


def create_app():
    from flask import Flask, jsonify
    app = Flask(__name__)

    @app.route('/channels/track', methods=['POST'])
    def track():
        return jsonify('Tracking')

    @app.route('/channels/messages')
    def messages():
        return jsonify(minute='2000', second='150')

    @app.route('/channels/mood')
    def mood():
        return jsonify(mood='Mind blowing ultra-hyped')

    return app


@pytest.fixture
def client():
    """
    Client fixture mocking database calls and App calls to the API
    :return: app client
    """
    app = create_app()
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True
    client = app.test_client()

    with app.app_context():
        db.init_db()

    yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])
