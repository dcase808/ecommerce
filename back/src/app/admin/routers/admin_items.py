from fastapi import APIRouter, Depends, UploadFile, HTTPException, status
from ..auth import get_current_user
from ...models import Item, ItemUpdate
from ...db_connect import bucket

router = APIRouter(
    prefix='/items',
    tags=['items'],
)

@router.get('', response_model=list[Item], dependencies=[Depends(get_current_user)])
async def get_items():
    return await Item.find().to_list()

@router.post('', response_model=Item, dependencies=[Depends(get_current_user)])
async def add_item(item: Item):
    return await item.insert()

@router.patch('', response_model=Item, dependencies=[Depends(get_current_user)])
async def update_item(data: ItemUpdate):
    updated_data = data.dict(exclude_unset=True, exclude={'id'})
    await Item.find_one({'_id': data.id}).update({'$set': updated_data})
    return await Item.find_one({'_id': data.id})

@router.post('/image')
async def upload_image(file: UploadFile):
    if file.content_type == 'image/png' or file.content_type == 'image/jpg':
        content = await file.read()
        bucket.upload_bytes(content, file.filename, file.content_type)
        return {'file_url': bucket.get_download_url(file.filename)}
    else:
        raise HTTPException(status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)