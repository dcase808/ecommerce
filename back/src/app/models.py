from decimal import Decimal
from pydantic import BaseModel, EmailStr, Field
from beanie import Document, PydanticObjectId
from datetime import datetime
import pymongo

class User(Document):
    id: str | None = Field(None)
    name: str | None = Field(None)
    address: str | None = Field(None)
    postal_code: str | None = Field(None)
    city: str | None = Field(None)

class UserCreate(User):
    id: EmailStr
    password: str

class UserInDB(User):
    social: bool | None = Field(False)
    key: bytes | None = None
    salt: bytes | None = None

class Token(BaseModel):
    access_token: str
    token_type: str

class Item(Document):
    title: str
    desc: str
    price: Decimal
    tags: list[str] | None = None

    class Settings:
        indexes = [
            [('title', pymongo.TEXT), ('tags', pymongo.TEXT)]
        ]

class ItemUpdate(Item):
    title: str | None = None
    desc: str | None = None
    price: Decimal | None = None
    tags: list[str] | None = None

class ItemsInOrder(BaseModel):
    id: PydanticObjectId
    quantity: int

class Order(Document):
    item: list[ItemsInOrder]

class OrderInDB(Order):
    user: str
    price: Decimal
    paid: bool = Field(False)
    date: datetime = Field(datetime.now())

class OrderOut(Order):
    price: Decimal
    paid: bool

class OrderUpdate(Order):
    user: str | None = None
    price: Decimal | None = None
    paid: bool | None = None
    date: datetime | None = None
    item: list[ItemsInOrder] | None = None

class Admin(Document):
    id: str

class AdminCreate(Admin):
    password: str

class AdminInDB(Admin):
    key: bytes
    salt: bytes