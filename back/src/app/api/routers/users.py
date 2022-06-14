from fastapi import APIRouter, Depends, HTTPException, status
from ..auth import get_current_user, hash_password, authenticate_user, create_token, verify_oidc_token
from fastapi.security import OAuth2PasswordRequestForm
from ...models import User, UserCreate, Token, UserInDB, Order, OrderInDB, OrderOut, Item
from beanie import PydanticObjectId

router = APIRouter(
    prefix='/users',
    tags=['users']
)

@router.post('/token', response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    token = create_token({'sub': form_data.username})
    return {'access_token': token, 'token_type': 'bearer'}

@router.post('/token/ouath', response_model=Token)
async def social_login(data = Depends(verify_oidc_token)):
    email, _ = data
    query = User.find_one({'_id': email, 'social': True})
    if await query is None:
        email, name = data
        query = UserInDB.find({'_id': email})
        out = UserInDB(id=email, name=name, social=True)
        token = create_token({'sub': email})
        return {'access_token': token, 'token_type': 'bearer'}
    token = create_token({'sub': email})
    return {'access_token': token, 'token_type': 'bearer'}

@router.post('/register', response_model=User)
async def register(user: UserCreate):
    query = UserInDB.find({'_id': user.id})
    if await query.count():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)
    key, salt = hash_password(user.password)
    out = UserInDB(**user.dict(), key=key, salt=salt)
    return await out.insert()

@router.delete('/me', response_model=User)
async def delete_user(user = Depends(get_current_user)):
    user = await User.find_one({'_id': user.id})
    await user.delete()
    return user

@router.get('/me', response_model=User)
async def get_user(user = Depends(get_current_user)):
    return user

@router.put('/me', response_model=User)
async def update_user(data: User, user = Depends(get_current_user)):
    updated_data = data.dict(exclude_unset=True, exclude={'id'})
    await User.find_one({'_id': user.id}).update({'$set': updated_data})
    return await User.find_one({'_id': user.id})

