import os
import tempfile
import json
import pytest
import datetime

from main import app, db

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{app.config['DATABASE']}"
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])


def test_route_test_index(client):
    res = client.get("/test/")
    assert res.status_code == 200
    assert res.data == b'bp_test_index'


def test_route_api_index(client):
    res = client.get("/api/")
    assert res.status_code == 200
    assert json.loads(res.data) == {
        'data': 'hello world'
    }


def test_route_api_clock(client):
    res = client.get("/api/utils/clock")
    assert res.status_code == 200
    server_response = json.loads(res.data)['data'].split('.')[0]
    now = datetime.datetime.now().isoformat().split('.')[0]
    assert server_response == now


def test_route_user_get(client):
    res = client.get("/user/")
    assert res.status_code == 200
    server_data = json.loads(res.data)
    assert len(server_data['data']) == 0


def test_route_user_create(client):
    res = client.post("/user/", data={
        "username": "test",
        "email": "test@example.it"
    })
    assert res.status_code == 200
    server_data = json.loads(res.data)
    assert server_data['id'] == 1


def test_route_user_get_by_id(client):
    # create entity
    res = client.post("/user/", data={
        "username": "test",
        "email": "test@example.it"
    })

    res = client.get("/user/1")
    assert res.status_code == 200
    server_data = json.loads(res.data)
    assert server_data['id'] == 1
    assert server_data['username'] == "test"
    assert server_data['email'] == "test@example.it"
