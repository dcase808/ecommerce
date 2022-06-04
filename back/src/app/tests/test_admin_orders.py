from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

def test_get_orders_no_auth():
    with TestClient(app) as client:
        response = client.get('/v1/admin/orders')
        assert response.status_code == 401

def add_order_no_auth():
    with TestClient(app) as client:
        response = client.post(
            '/v1/admin/orders',
            json={'item':
            {
                'id': 1,
                'quantity': 0
            }})
        assert response.status_code == 401

def get_order_by_id_no_auth():
    with TestClient(app) as client:
        response = client.get('/v1/admin/orders/1')
        assert response.status_code == 401