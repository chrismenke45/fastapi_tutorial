from app import schemas
from .database import client, session
import pytest


@pytest.fixture
def test_user(client):
    user_data = {"email": "bob@gmail.com", "password": "pass123"} 
    res = client.post("/users/", json=user_data)
    assert res.status_code == 201
    new_user = res.json()
    new_user["password"] = user_data["password"]
    return new_user


# def test_root(client):
#     res = client.get('/')
#     print(res.json().get("message"))
#     assert res.json().get("message") == "Hello World"
#     assert res.status_code == 200

def test_create_user(client):
    res = client.post('/users/', json={"email": "hellow@gmail.com", "password": "pass123"})
    print(res.json())
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "hellow@gmail.com"
    assert res.status_code == 201

def test_login_user(client, test_user):
    res = client.post('/login', data={"username": test_user["email"], "password": test_user["password"]})
    assert res.status_code == 200