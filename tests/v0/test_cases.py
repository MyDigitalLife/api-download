from flask import url_for
from uuid import uuid4, UUID
import json


def test_index_returns_stream_for_existing_uuid(app, client):
    with app.app_context():
        # TODO: make sure this passed UUID is always recent and exists
        res = client.get(
            url_for("v0.cases.index", uuid=UUID("37ef60df-2183-428d-b651-4c3f3cd94ebb"))
        )
        assert res.status_code == 200
        assert res.is_streamed


def test_index_returns_stream_for_random_uuid(app, client):
    with app.app_context():
        res = client.get(url_for("v0.cases.index", uuid=uuid4()))
        assert res.status_code == 200
        assert res.is_streamed


def test_index_fails_without_args(app, client):
    with app.app_context():
        res = client.get(url_for("v0.cases.index"))
        assert res.status_code == 400
        assert json.dumps(json.loads(res.data), sort_keys=True) == json.dumps(
            {"code": 400, "message": "No valid UUID for the requested query",},
            sort_keys=True,
        )
