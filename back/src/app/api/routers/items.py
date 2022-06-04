from fastapi import APIRouter, Depends
from ..auth import get_current_user
from ...models import Item

router = APIRouter(
    prefix='/items',
    tags=['items'],
)

@router.get('', response_model=list[Item])
async def get_items():
    return await Item.find().to_list()

@router.post('', response_model=Item)
async def add_item(item: Item):
    return await item.insert()