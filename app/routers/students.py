"""
This file will contain routes for setting and getting student data.
"""

# import fastapi stuff
from fastapi import APIRouter, Response, HTTPException
from services.assistanceMongoDB import MongoService
from models.StudentModels import (
    StudentModel,
    StudentResponseModel,
    EncodingModel,
    EncodingResponseModel,
)
from models.PanelModels import PanelID

# import db
from pymongo.errors import PyMongoError

router = APIRouter(prefix="/student", tags=["Students"])


@router.get("/test", status_code=200, summary="Test route")
def index():
    return Response(content="Hello, World!", status_code=200)


@router.post(
    "/add_student",
    status_code=200,
    summary="Add a student",
    response_model=StudentResponseModel,
)
def add_student(student: StudentModel):
    # add the student to the database
    try:
        # instantiate the mongo service
        mongo_obj = MongoService()
        # call the function from mongo service to add the student
        student_response = mongo_obj.add_student(student)
        
        
        print(student_response)
        return StudentResponseModel(
            _id=student_response._id,
            name=student_response.name,
            prn=student_response.prn,
            panel=student_response.panel,
            panel_roll_no=student_response.panel_roll_no,
        )
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post(
    "/get_student_from_panel_id", status_code=200, summary="Get students from panel id"
)
def get_students_from_panel_id(panel_id: PanelID):
    try:
        # instantiate the mongo service
        mongo_obj = MongoService()
        # call the mongo function to get the student from panel
        students = mongo_obj.get_student_by_panel_id(panel_id.panel_id)
        return students
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post(
    "/get_student_encoding",
    status_code=200,
    summary="Get student encoding From student ID",
)
def get_student_encoding(student_encoding_model: EncodingModel):
    # get student_id
    student_id = student_encoding_model.student_id
    try:
        # instantiate the mongo service
        mongo_obj = MongoService()
        # call the function from mongo service to get the student encoding
        student_encoding = mongo_obj.get_student_encoding_from_student_id(student_id)
        print(student_encoding)
        encoding_response_model = EncodingResponseModel(
            student_id=student_id,
            number_of_faces=student_encoding["number_of_faces"],
            encoding_url=student_encoding["encoding"],
        )
        return encoding_response_model
    except PyMongoError as e:
        raise HTTPException(status_code=503, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# route for getting all students
@router.get("/get_all_students", status_code=200, summary="Get all students")
def get_all_students():
    try:
        # instantiate the mongo service
        mongo_obj = MongoService()
        # call the function from mongo service to get all students
        students = mongo_obj.get_all_students()
        return students
    except PyMongoError as e:
        raise HTTPException(status_code=503, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
