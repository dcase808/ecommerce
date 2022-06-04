from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

def test_get_items():
    with TestClient(app) as client:
        response = client.get('/v1/api/items')
        assert response.status_code == 200
