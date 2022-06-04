from fastapi import HTTPException
from fastapi.testclient import TestClient
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import pytest

from ..api.routers.payments_misc import auth_payu
from ..main import app
from ..secrets import PAYU_POS, PAYU_MD5

client = TestClient(app)

def test_login_correct():
    with TestClient(app) as client:
        response = client.post('/v1/api/users/token', data={'username': 'admin', 'password': 'admin'})
        assert response.status_code == 200
        assert response.json()

def test_login_incorrect():
    with TestClient(app) as client:
        response = client.post('/v1/api/users/token', data={'username': 'test', 'password': 'tes'})
        assert response.status_code == 401

def test_login_incorrect_password():
    with TestClient(app) as client:
        response = client.post('/v1/api/users/token', data={'username': 'admin', 'password': 'tes'})
        assert response.status_code == 401

def test_login_wrong_data():
    with TestClient(app) as client:
        response = client.post('/v1/api/users/token', data={'user': 'admin', 'pass': 'tes'})
        assert response.status_code == 422

def test_payu_auth():
    auth_payu(HTTPBasicCredentials(username=PAYU_POS, password=PAYU_MD5))

def test_payu_auth_bad_credentials():
    with pytest.raises(HTTPException):
        auth_payu(HTTPBasicCredentials(username='test', password='test'))