'''
This file contains routes for getting and setting data about subjects and semesters. 
'''

# import fastapi stuff
from fastapi import APIRouter, Response

router = APIRouter(prefix="/subjects", tags=["Subjects and Semesters"])


@router.get("/test", status_code=200, summary="Test route")
def index():
    return Response(content="Hello, World!", status_code=200)
