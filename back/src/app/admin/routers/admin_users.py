from fastapi import APIRouter, Depends, HTTPException, status
from ..auth import get_current_user, hash_password, authenticate_user, create_token
from fastapi.security import OAuth2PasswordRequestForm
from ...models import Admin, AdminCreate, AdminInDB, User, UserCreate, Token, UserInDB, Order, OrderInDB, OrderOut, Item
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

@router.post('/add-admin', response_model=Admin, dependencies=[Depends(get_current_user)])
async def register(user: AdminCreate):
    query = AdminInDB.find({'_id': user.id})
    if await query.count():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)
    key, salt = hash_password(user.password)
    out = AdminInDB(**user.dict(), key=key, salt=salt)
    return await out.insert()

@router.get('/', response_model=list[User], dependencies=[Depends(get_current_user)])
async def get_users():
    return await User.find().to_list()

@router.patch('/', response_model=User, dependencies=[Depends(get_current_user)])
async def update_user(data: User):
    updated_data = data.dict(exclude_unset=True, exclude={'id'})
    await User.find_one({'_id': data.id}).update({'$set': updated_data})
    return await User.find_one({'_id': data.id})

@router.get('/me')
async def get_current_admin(user = Depends(get_current_user)):
    return {'user': 'admin'}