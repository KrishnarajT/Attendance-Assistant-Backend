from fastapi import APIRouter, File, UploadFile, Response
from services.assistanceFirebase import AssistanceFirebase

# import models
from models.AttendanceModels import AttendanceModel

fb_storage = AssistanceFirebase()

router = APIRouter(
    prefix="/upload", tags=["Upload Images or Attendance Info from App/Website/Pi"]
)


@router.post("/add_image")
async def upload_image(image: UploadFile = File(...)):
    """
    Uploads an image to the server
    :param image: Image to be uploaded, that has a face ideally.
    :return: URL of the uploaded image.
    """
    image_data = await image.read()
    image_url = fb_storage.upload_image(image_data)
    return {"image_url": image_url}


@router.post("/add_attendance", response_model=AttendanceModel)
async def add_attendance(attModel: AttendanceModel):
    """
    Adds attendance to the database
    :param attModel: Attendance model that contains all the necessary information
    :return: URL of the uploaded image.
    """
    # add attendance to the database
    pass
    return Response(status_code=200, content=attModel)
