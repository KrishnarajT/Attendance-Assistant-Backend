"""
This file contains routes for getting and setting data about subjects and semesters. 
"""

from pymongo.errors import PyMongoError

# import fastapi stuff
from fastapi import APIRouter, Response, HTTPException

# import models
from models.SubjectModels import Subject

# import the assistance service
from models.PanelModels import SemesterModel

# import the services
from services.teacher_and_subject_services import (
    add_subject,
    get_all_subjects,
)

from services.panel_services import add_semester, get_all_semesters

router = APIRouter(prefix="/subjects", tags=["Subjects and Semesters"])


@router.get("/test", status_code=200, summary="Test route")
def index_route():
    return Response(content="Hello, World!", status_code=200)


@router.post("/add_subject", status_code=201, summary="Add a subject")
def add_subject_route(subject: Subject):
    """
    This route adds a subject to the database.
    : param subject: The subject to be added.
    : return: The added subject.
    """
    try:
        added_subject = add_subject(subject)
        if added_subject:
            return added_subject
        else:
            raise HTTPException(
                status_code=500, detail="An error occurred while adding the subject"
            )
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))


# Get all subjects
@router.get("/get_all_subjects", status_code=200, summary="Get all subjects")
def get_all_subjects_route():
    """
    This route gets all the subjects from the database.
    : return: A list of all the subjects in the database.
    """
    try:
        all_subjects = get_all_subjects()
        if all_subjects:
            return all_subjects
        else:
            raise HTTPException(
                status_code=500, detail="An error occurred while getting all subjects"
            )
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/add_semester", status_code=201, summary="Add a semester")
def add_semester_route(semester: SemesterModel):
    """
    This route adds a semester to the database.
    : param semester: The semester to be added.
    : return: The added semester.
    """
    try:
        added_semester = add_semester(semester)
        if added_semester:
            return added_semester
        else:
            raise HTTPException(
                status_code=500, detail="An error occurred while adding the semester"
            )
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/get_all_semesters", status_code=200, summary="Get all semesters")
def get_all_semesters_route():
    """
    This route gets all the semesters from the database.
    : return: A list of all the semesters in the database.
    """
    try:
        all_semesters = get_all_semesters()
        if all_semesters:
            return all_semesters
        else:
            raise HTTPException(
                status_code=500, detail="An error occurred while getting all semesters"
            )
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))
