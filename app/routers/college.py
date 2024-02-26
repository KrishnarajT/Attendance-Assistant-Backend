"""
This includes routes for getting and setting data about rooms and buildings. 
"""

# import fastapi stuff
from fastapi import APIRouter, Response

router = APIRouter(prefix="/college", tags=["Rooms and Buildings"])


@router.get("/test", status_code=200, summary="Test route")
def index():
    return Response(content="Hello, World!", status_code=200)
