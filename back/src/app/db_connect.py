from .secrets import CONNECTION_STRING, B2_KEY_ID, B2_APPLICATION_KEY
from beanie import init_beanie
import motor.motor_asyncio
from .models import Item, User, Order, Admin
from b2sdk.v2 import InMemoryAccountInfo, B2Api

async def init():
    client = motor.motor_asyncio.AsyncIOMotorClient(CONNECTION_STRING)
    await init_beanie(database=client.shopv2, document_models=[User, Item, Order, Admin])

def init_image_storage():
    info = InMemoryAccountInfo()
    b2_api = B2Api(info)
    b2_api.authorize_account('production', B2_KEY_ID, B2_APPLICATION_KEY)
    return b2_api.get_bucket_by_name('ecommerce-36431')

bucket = init_image_storage()