from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 404

def test_get_main_api():
    response = client.get("/v1/api/")
    assert response.status_code == 404

def test_get_main_admin():
    response = client.get("/v1/admin/")
    assert response.status_code == 404