from re import A
from beanie import PydanticObjectId
from fastapi import APIRouter, Depends, HTTPException, Query, status
from ..auth import get_current_user
from ...models import Item
from beanie.operators import In

router = APIRouter(
    prefix='/items',
    tags=['items'],
)

@router.get('', response_model=list[Item])
async def get_items(tag: str | None = Query(None)):
    if tag:
        return await Item.find(In(Item.tags, [tag])).to_list()
    else:
        return await Item.find().to_list()

@router.get('/search', response_model=list[Item])
async def search_items(query: str):
    return await Item.find({'$text': {'$search': f'"{query}"'}}).to_list()

@router.get('/{id}', response_model=Item)
async def get_item(id: str):
    try:
        PydanticObjectId(id)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return await Item.get(id)