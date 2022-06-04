from datetime import datetime, timedelta
from os import urandom
from hashlib import pbkdf2_hmac
from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer, OAuth2AuthorizationCodeBearer
from ..secrets import SECRET_KEY, CLIENT_ID, CLIENT_SECRET
from ..models import User, UserInDB
from google.oauth2 import id_token
from google.auth.transport import requests

ouath2_user = OAuth2PasswordBearer(tokenUrl='users/token')

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def hash_password(password):
    salt = urandom(32)
    key = pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        10000
    )
    return key, salt

def verify_password(password, key, salt):
    new_key = pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        10000
    )
    if new_key == key:
        return True
    return False

async def authenticate_user(username, password):
    query = User.find({'_id': username, 'social': False})
    if await query.count() > 0:
        user = await UserInDB.find_one({'_id': username})
        if verify_password(password, user.key, user.salt):
            return True
    return False

def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: str = Depends(ouath2_user)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username = payload.get('sub')
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    query = User.find({'_id': username})
    if await query.count() > 0:
        return await User.find_one({'_id': username})
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

def verify_oidc_token(token: str):
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return idinfo['email'], idinfo['name']