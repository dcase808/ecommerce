from fastapi import APIRouter, Depends, HTTPException, status
from ..auth import get_current_user
from ...models import Order, OrderInDB, OrderOut, Item
from beanie import PydanticObjectId

router = APIRouter(
    prefix='/orders',
    tags=['orders'],
)

@router.post('', response_model=OrderOut)
async def create_order(order: Order, user = Depends(get_current_user)):
    price = 0
    for item in order.item:
        if item.quantity < 1:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        try:
            current_item = await Item.find_one({'_id': item.id})
            price += current_item.price * item.quantity
        except:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    order_updated = OrderInDB(**order.dict(), user=user.id, price=price)
    return await order_updated.insert()

@router.get('/{id}', response_model=OrderOut)
async def get_order_by_id(id: PydanticObjectId, user = Depends(get_current_user)):
    order = await OrderOut.find_one({'_id': id, 'user': user.id})
    if order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return order

@router.get('', response_model=list[OrderOut])
async def get_orders(user = Depends(get_current_user)):
    return await OrderOut.find({'user': user.id}).to_list()