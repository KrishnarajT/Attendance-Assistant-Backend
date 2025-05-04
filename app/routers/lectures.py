# import fastapi stuff
from fastapi import APIRouter


# import db stuff

# import models
from models.lectureModels import lectureModel

router = APIRouter(prefix="/lectures", tags=["Lectures"])

# import lecture service
from services.lecture_services import (
    add_lecture,
    get_lecture,
    get_all_lectures,
    get_lecture_images_between_time_on_date,
)


@router.post("/add_lecture", status_code=200, summary="Add a lecture")
def add_lecture_route(lecture_details: lectureModel):
    """
    Add a lecture to the database.
    """
    # call the function from lecture services to add the lecture
    lecture_response = add_lecture(lecture_details)
    return lecture_response


@router.get("/get_lecture", status_code=200, summary="Get a lecture")
def get_lecture_route(lecture_id: str):
    """
    Get a lecture from the database.
    """
    # call the function from lecture services to get the lecture
    lecture_response = get_lecture(lecture_id)
    return lecture_response


@router.get("/get_all_lectures", status_code=200, summary="Get all lectures")
def get_all_lectures_route():
    """
    Get all lectures from the database.
    """
    # call the function from lecture services to get all the lectures
    lecture_response = get_all_lectures()
    return lecture_response


@router.get(
    "/get_lecture_images_between_time",
    status_code=200,
    summary="Get all lecture images between a start and end time",
)
def get_lecture_images_between_time_route(
    start_time: str, end_time: str, given_date: str
):
    """
    Get all lecture images between a start and end time.
    """
    # call the function from lecture services to get all the lecture images between the start and end time
    lecture_response = get_lecture_images_between_time_on_date(
        start_time, end_time, given_date
    )
    return lecture_response
