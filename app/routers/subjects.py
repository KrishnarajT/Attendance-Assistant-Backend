'''
This file contains routes for getting and setting data about subjects and semesters. 
'''


from pymongo.errors import PyMongoError
# import fastapi stuff
from fastapi import APIRouter, Response, HTTPException

#import models
from models.SubjectModels import Subject

# import the assistance service
from services.assistanceMongoDB import AssistanceService

router = APIRouter(prefix="/subjects", tags=["Subjects and Semesters"])


@router.get("/test", status_code=200, summary="Test route")
def index():
    return Response(content="Hello, World!", status_code=200)


@router.post("/add_subject", status_code=201, summary="Add a subject")
def add_subject(subject: Subject):
    """
    This route adds a subject to the database.
    : param subject: The subject to be added.
    : return: The added subject.
    """
    try:
        add_subject_service = AssistanceService()
        added_subject = add_subject_service.add_subject(subject)
        if added_subject:
            return added_subject
        else:
            raise HTTPException(status_code=500, detail="An error occurred while adding the subject")
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# Get all subjects
@router.get("/get_all_subjects", status_code=200, summary="Get all subjects")
def get_all_subjects():
    """
    This route gets all the subjects from the database.
    : return: A list of all the subjects in the database.
    """
    try:
        get_all_subjects_service = AssistanceService()
        all_subjects = get_all_subjects_service.get_all_subjects()
        if all_subjects:
            return all_subjects
        else:
            raise HTTPException(status_code=500, detail="An error occurred while getting all subjects")
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))