import pytest


import models

from init_app import db
from main import app
from utils import TASK_STATUS


@pytest.fixture
def test_app():
    app.config['TESTING'] = True

    with app.app_context():
        db.create_all()
        for name in TASK_STATUS:
            status = models.Status(
                name=name,
            )
            db.session.add(status)
            db.session.commit()

    yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(test_app):
    """A test client for the app."""
    return app.test_client()
