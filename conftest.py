from tokenize import String

from flask import Flask
import pytest  # type: ignore
from flask.testing import FlaskClient
from werkzeug import Client

from app import create_app


@pytest.fixture  # type: ignore
def app() -> Flask:
    app = create_app()
    return app


@pytest.fixture
def client(app) -> FlaskClient:
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
