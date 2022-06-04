from .secrets import CONNECTION_STRING
from beanie import init_beanie
import motor.motor_asyncio
from .models import Item, User, Order, Admin

async def init():
    client = motor.motor_asyncio.AsyncIOMotorClient(CONNECTION_STRING)
    await init_beanie(database=client.shopv2, document_models=[User, Item, Order, Admin])