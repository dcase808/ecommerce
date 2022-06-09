from fastapi import FastAPI, HTTPException, status
from .api.routers import items, users, orders, payments
from .admin.routers import admin_items, admin_users, admin_orders
from fastapi.middleware.cors import CORSMiddleware
from .db_connect import init

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_headers=['*'],
    allow_methods=['*']
)

@app.on_event('startup')
async def startup_event():
    await init()

@app.get('', include_in_schema=False)
async def root():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

api = FastAPI()

@api.get('/', include_in_schema=False)
async def root():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
api.include_router(items.router)
api.include_router(users.router)
api.include_router(orders.router)
api.include_router(payments.router)

admin = FastAPI()

@admin.get('/', include_in_schema=False)
async def root():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

admin.include_router(admin_users.router)
admin.include_router(admin_items.router)
admin.include_router(admin_orders.router)

app.mount('/v1/api', api)
app.mount('/v1/admin', admin)