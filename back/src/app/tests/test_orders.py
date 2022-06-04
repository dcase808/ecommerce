from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

def test_get_orders_no_auth():
    with TestClient(app) as client:
        response = client.get('/v1/api/orders')
        assert response.status_code == 401

def add_order_no_auth():
    with TestClient(app) as client:
        response = client.get(
            '/v1/api/orders',
            json={'item':
            {
                'id': 1,
                'quantity': 0
            }})
        assert response.status_code == 401