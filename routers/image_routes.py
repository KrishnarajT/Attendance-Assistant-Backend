# fastapi router file
# Path: routers/image_routes.py
from fastapi import APIRouter
from fastapi import File


router = APIRouter()

@app.get("/add_image")
def index():
	return {"message": "Hello World"}
