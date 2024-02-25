from fastapi import APIRouter


router = APIRouter()

@router.get("/test")
def index():
	return {"message": "First code in Fast API"}
