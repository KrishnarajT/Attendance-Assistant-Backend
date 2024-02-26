"""
This contains routes for getting and setting data from the classes and the ClassImages Collections.
"""

# import fastapi stuff
from fastapi import APIRouter, Response
#import mongodb client

router = APIRouter(prefix="/classes", tags=["Classes and Class Images"])


@router.get("/test", status_code=200, summary="Test route")
def index():
    return Response(content="Hello, World!", status_code=200)
