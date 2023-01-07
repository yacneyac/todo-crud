import pytest

import models
from init_app import db
from main import app


@pytest.fixture
def test_app():
    # db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    # with app.test_client() as client:
    with app.app_context():
        db.drop_all()
        db.create_all()
        for name in ['new', 'done', 'in_work']:
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