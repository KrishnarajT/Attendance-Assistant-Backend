"""
This file will contain routes for setting and getting student data.
"""

# import fastapi stuff
from fastapi import APIRouter, Response
from models.StudentModels import StudentModel, StudentResponseModel

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
    student_response = StudentResponseModel(
        student_id=student.student_id,
        student_name=student.student_name,
        student_email=student.student_email,
        student_phone=student.student_phone,
        student_address=student.student_address,
    )
    return student_response
