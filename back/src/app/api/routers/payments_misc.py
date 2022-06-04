from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from ...secrets import PAYU_MD5, PAYU_POS, PAYU_SECRET
from ...models import Item
import requests
from secrets import compare_digest

payu_auth = HTTPBasic()

def auth_payu(credentials: HTTPBasicCredentials = Depends(payu_auth)):
    user = compare_digest(credentials.username, str(PAYU_POS))
    password = compare_digest(credentials.password, PAYU_MD5)
    if not (user and password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

def get_payu_token():
    data = {
        'grant_type': 'client_credentials',
        'client_id': PAYU_POS,
        'client_secret': PAYU_SECRET
    }
    response = requests.post('https://secure.snd.payu.com/pl/standard/user/oauth/authorize', data=data)
    return response.json()['access_token']

async def get_products_in_order(order):
    products = []
    for product in order.item:
        item = await Item.find_one({'_id': product.id})
        entry = {}
        entry['name'] = item.title
        entry['unitPrice'] = int(item.price * 100)
        entry['quantity'] = product.quantity
        products.append(entry)
    return products

async def create_payment_request(order, ip):
    access_token = get_payu_token()

    products = await get_products_in_order(order)
    
    data = {
        'notifyUrl': "https://ecommerce-demo-api.herokuapp.com/payments/confirm",
        "customerIp": ip,
        'merchantPosId': PAYU_POS,
        'description': 'Zamowienie '+ str(order.id),
        'currencyCode': 'PLN',
        'totalAmount': int(order.price*100),
        'extOrderId': str(order.id),
        'products': products
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + access_token
    }
    response = requests.post(
        'https://secure.snd.payu.com/api/v2_1/orders',
        headers=headers,
        json=data,
        allow_redirects=False
    )
    return response.json()