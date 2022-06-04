from fastapi.testclient import TestClient
from ..main import app
from ..api.routers.payments_misc import get_products_in_order

client = TestClient(app)

def test_get_products_in_order():
    pass
