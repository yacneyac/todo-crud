import pytest


import models

from init_app import db
from main import app as main_app
from utils import TASK_STATUS


@pytest.fixture
def app():
    """Make test Flask app for every test case"""
    main_app.config['TESTING'] = True

    with main_app.app_context():
        db.drop_all()
        db.create_all()
        for name in TASK_STATUS:
            status = models.Status(
                name=name,
            )
            db.session.add(status)
            db.session.commit()

    yield main_app

    with main_app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    """A test client for the Flask app"""
    return main_app.test_client()
