"""
This contains routes for getting and setting data from the Lecture and the LectureImages Collections.
"""

# import fastapi stuff
from fastapi import APIRouter, HTTPException, Response
#import mongodb client
from services.assistanceMongoDB import MongoService

# import models
from models.lectureModels import lectureModel, lectureModelId
router = APIRouter(prefix="/classes", tags=["Classes and Class Images"])


@router.get("/test", status_code=200, summary="Test route")
def index():
    return Response(content="Hello, World!", status_code=200)


@router.post( "/add_lecture", status_code=200, summary="Add a lecture")
def add_lecture( lecture: lectureModel):
    """
    Add a lecture to the database.
    """
    # add the lecture to the database
    try:
        # instantiate the mongo service
        mongo_obj = MongoService()
        # call the function from mongo service to add the lecture
        lecture_response = mongo_obj.add_lecture(lecture)
        return lecture_response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post( "/get_lecture_by_id", status_code=200, summary="Get a lecture")
def get_lecture( lecture_id: lectureModelId):
    """
    Get a lecture from the database.
    """
    # get the lecture from the database
    try:
        # instantiate the mongo service
        mongo_obj = MongoService()
        # call the function from mongo service to get the lecture
        lecture_response = mongo_obj.get_lecture(lecture_id.lec_id)
        return lecture_response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/get_all_lectures", status_code=200, summary="Get all lectures")
def get_all_lectures():
    """
    Get all lectures from the database.
    """
    # get all the lectures from the database
    try:
        # instantiate the mongo service
        mongo_obj = MongoService()
        # call the function from mongo service to get all the lectures
        lecture_response = mongo_obj.get_all_lectures()
        return lecture_response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))