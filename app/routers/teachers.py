"""
This contains routes for getting and setting data from the teachers Collection.
"""

# import fastapi stuff
from fastapi import APIRouter, Response, HTTPException
# import the teacher model
from models.TeacherModels import Teacher, TeacherInDB
#import the assistance service
from services.assistanceMongoDB import AssistanceService
#import pymongo errors
from pymongo.errors import PyMongoError



router = APIRouter(prefix="/teachers", tags=["Teachers"])


@router.get("/test", status_code=200, summary="Test route")
def index():
    return Response(content="Hello, World!", status_code=200)

# Add a teacher
@router.post("/add_teacher", status_code=201, summary="Add a teacher")
def add_teacher(teacher: Teacher):
    try:
        add_teacher_service = AssistanceService()
        added_teacher = add_teacher_service.add_teacher(teacher)
        if added_teacher:
            return added_teacher
        else:
            raise HTTPException(status_code=500, detail="An error occurred while adding the teacher")
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))
    

# Get all teachers
@router.get("/get_all_teachers", status_code=200, summary="Get all teachers")
def get_all_teachers():
    try:
        get_all_teachers_service = AssistanceService()
        all_teachers = get_all_teachers_service.get_all_teachers()
        if all_teachers:
            return all_teachers
        else:
            raise HTTPException(status_code=500, detail="An error occurred while getting all teachers")
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))

# Get a teacher by id
@router.post("/get_teacher_by_id", status_code=200, summary="Get a teacher by id")
def get_teacher_by_id(teacher_id: TeacherInDB):
    try:
        get_teacher_by_id_service = AssistanceService()
        teacher = get_teacher_by_id_service.get_teacher_by_id(teacher_id)
        if teacher:
            return teacher.to_dict()
        else:
            raise HTTPException(status_code=500, detail="An error occurred while getting the teacher")
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))