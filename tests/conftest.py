import os
from flask_mongoengine import MongoEngine
import pytest
from app import create_app



@pytest.fixture(scope='session')
def app():
    """Create and configure an instance of the Flask application."""
    app = create_app(config_name='test')
    yield app

@pytest.fixture(scope='function')
def client(app):
    """Create a test client for the Flask application."""
    yield app.test_client()
