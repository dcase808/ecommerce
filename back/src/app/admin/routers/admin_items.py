from fastapi import APIRouter, Depends
from ..auth import get_current_user
from ...models import Item, ItemUpdate

router = APIRouter(
    prefix='/items',
    tags=['items'],
)

@router.get('', response_model=list[Item], dependencies=[Depends(get_current_user)])
async def get_items():
    return await Item.find().to_list()

@router.post('', response_model=Item, dependencies=[Depends(get_current_user)])
async def add_item(item: Item):
    return await item.insert()

@router.patch('/', response_model=Item, dependencies=[Depends(get_current_user)])
async def update_item(data: ItemUpdate):
    updated_data = data.dict(exclude_unset=True, exclude={'id'})
    await Item.find_one({'_id': data.id}).update({'$set': updated_data})
    return await Item.find_one({'_id': data.id})