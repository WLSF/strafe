import os
import pytest
import tempfile

from api.src.main import create_app
from api.src import db


@pytest.fixture
def app():
    """
    App fixture mocking database calls and App calls to the API
    :return: app
    """

    app = create_app()
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True
    db.setup_db(app)

    with app.app_context():
        db.init_db()

    yield app

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])


@pytest.fixture
def client(app):
    """
    Client fixture mocking database calls and App calls to the API
    :return: client
    """
    return app.test_client()
