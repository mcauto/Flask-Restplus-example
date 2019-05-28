import pytest
from app import create_app  # flask application factory
from app import db

@pytest.fixture(scope='session')
def flask_app():
    app = create_app('test')
    db.init_app(app) # Integrity test
    app_context = app.app_context()
    app_context.push()
    return app

