import pytest  # type: ignore
from flask import Flask
from flask.testing import FlaskClient

from app import create_app


@pytest.fixture  # type: ignore
def app() -> Flask:
    app = create_app()
    return app


@pytest.fixture  # type: ignore
def client(app: Flask) -> FlaskClient:  # type: ignore
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
