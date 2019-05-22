import pytest
from app import create_app  # flask application factory

@pytest.fixture(scope='session')
def flask_app():
    app = create_app('test')
    app_context = app.app_context()
    app_context.push()
    yield app
    app_context.pop()