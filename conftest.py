import pytest  # type: ignore
from flask import Flask
from flask.testing import FlaskClient

from app import create_app


@pytest.fixture  # type: ignore
def app() -> Flask:
    app = create_app()
    return app
