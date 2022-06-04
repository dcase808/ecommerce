from hashlib import md5
from fastapi import APIRouter, Depends, Request, HTTPException, status, Request
from ..auth import get_current_user
from ...models import Item, Order, OrderInDB, OrderOut
from beanie import PydanticObjectId
from ...secrets import PAYU_POS, PAYU_SECRET, PAYU_MD5
from .payments_misc import create_payment_request, auth_payu

router = APIRouter(
    prefix='/payments',
    tags=['payments'],
)
@router.post('/confirm', dependencies=[Depends(auth_payu)], include_in_schema=False)
async def confirm_payment(request: Request):
    try:
        body = await request.json()
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if body['order']['status'] == 'COMPLETED':
        order_id = body['order']['extOrderId']
        await OrderInDB.find_one({'_id': PydanticObjectId(order_id)}).update({'$set': {'paid': True}})

@router.post('')
async def create_payment(order_id: PydanticObjectId, request: Request, user = Depends(get_current_user)):
    order = await OrderInDB.find_one({'_id': order_id})
    if order.user != user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if order.paid:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE)
    return await create_payment_request(order, request.client.host)
