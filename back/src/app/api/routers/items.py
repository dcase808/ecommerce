from re import A
from fastapi import APIRouter, Depends, Query
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
    return await Item.get(id)