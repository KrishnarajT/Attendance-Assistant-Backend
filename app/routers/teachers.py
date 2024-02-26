"""
This contains routes for getting and setting data from the teachers Collection.
"""

# import fastapi stuff
from fastapi import APIRouter, Response

router = APIRouter(prefix="/teachers", tags=["Teachers"])


@router.get("/test", status_code=200, summary="Test route")
def index():
    return Response(content="Hello, World!", status_code=200)
