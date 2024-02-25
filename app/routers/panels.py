'''
This file will have routes for getting and setting panel data, school data, and specialization data. 
'''

# import fastapi stuff
from fastapi import APIRouter, Response

router = APIRouter(prefix="/panels", tags=["Panels, Schools and Specializations"])


@router.get("/test", status_code=200, summary="Test route")
def index():
    return Response(content="Hello, World!", status_code=200)
