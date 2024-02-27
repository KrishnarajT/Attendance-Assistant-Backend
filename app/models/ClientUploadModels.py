from datetime import date, time, datetime
from pydantic import BaseModel, field_validator


class AttendanceModel(BaseModel):
    room_id: str
    subject_id: str
    teacher_id: str
    panel_id: str
    start_time: datetime
    end_time: datetime

    @field_validator("start_time")
    def start_time_must_be_before_end_time(cls, v, values):
        pass

    @field_validator("end_time")
    def end_time_must_be_after_start_time(cls, v, values):
        pass

    @field_validator("start_time")
    def date_format(cls, v):
        v = "%Y-%m-%d %H:%M:%S"
        try:
            datetime.strptime(v, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            raise ValueError("Incorrect date format, should be YYYY-MM-DD HH:MM:SS")


class AddFaceModel(BaseModel):
    student_id: str
    face_image: bytes  # the image of the face to be added. from fastapi uploads.


class AddFaceResponseModel(BaseModel):
    student_id: str
    face_image_url: str  # from the place face image is stored.


class AddClassPhotoModel(BaseModel):
    room_id: str
    date: str
    time: str

    # # date must follow the format YYYY-MM-DD HH:MM:SS
    # @field_validator("date")
    # def date_format(cls, v):
    #     v = "%Y-%m-%d"
    #     try:
    #         datetime.strptime(v, "%Y-%m-%d")
    #     except ValueError:
    #         raise ValueError("Incorrect date format, should be YYYY-MM-DD")

    # # time must follow the format HH:MM:SS
    # @field_validator("time")
    # def time_format(cls, v):
    #     v = "%H:%M:%S"
    #     try:
    #         datetime.strptime(v, "%H:%M:%S")
    #     except ValueError:
    #         raise ValueError("Incorrect time format, should be HH:MM:SS")


class AddClassPhotoResponseModel(BaseModel):
    room_id: str
    date: str
    time: str
    class_photo_url: str  # from the place class photo is stored.


class FaceEncodingModel(BaseModel):
    student_id: str
    number_of_faces: int
    encoding: bytes


class FaceEncodingResponseModel(BaseModel):
    student_id: str
    number_of_faces: int
    encoding_url: str  # from the place encoding is stored.
