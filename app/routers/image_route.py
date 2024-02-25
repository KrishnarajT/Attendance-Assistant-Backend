
from fastapi import APIRouter, UploadFile, File
from services.assistanceFirebase import AssistanceFirebase
router = APIRouter()
fb_storage = AssistanceFirebase()

@router.post("/add_image")
async def add_image(image: UploadFile = File(...)):
    image_data = await image.read()
    image_url = fb_storage.upload_image(image_data)
    return {"image_url": image_url}
    