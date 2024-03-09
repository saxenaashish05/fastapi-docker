from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_random_user_unauthorized():
    credentials = ("incorrect_saxena", "incorrect_ashish")
    response = client.get("/user", auth=credentials)
    assert response.status_code == 401
    assert "Unauthorized" in response.text

def test_get_random_user():
    credentials = ("ashish", "saxena")
    response = client.get("/user", auth=credentials)
    assert response.status_code == 200
    assert "name" in response.json()
    assert "password" in response.json()