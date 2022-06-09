from fastapi import APIRouter, Depends, HTTPException, status
from ..auth import get_current_user
from ...models import Order, OrderInDB, OrderUpdate, OrderOut, Item
from beanie import PydanticObjectId

router = APIRouter(
    prefix='/orders',
    tags=['orders'],
)

@router.get('/{id}', response_model=OrderInDB, dependencies=[Depends(get_current_user)])
async def get_order_by_id(id: PydanticObjectId):
    order = await OrderInDB.find_one({'_id': id})
    if order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return order

@router.get('', response_model=list[OrderInDB], dependencies=[Depends(get_current_user)])
async def get_orders():
    return await OrderInDB.find().to_list()

@router.patch('/', response_model=OrderInDB, dependencies=[Depends(get_current_user)])
async def update_order(data: OrderUpdate):
    updated_data = data.dict(exclude_unset=True, exclude={'id'})
    await Order.find_one({'_id': data.id}).update({'$set': updated_data})
    return await OrderInDB.find_one({'_id': data.id})