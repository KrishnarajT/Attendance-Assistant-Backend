from datetime import datetime
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
    # date must follow the format YYYY-MM-DD HH:MM:SS
    @field_validator("start_time")
    def date_format(cls, v):
        v="%Y-%m-%d %H:%M:%S"
        try:
            datetime.strptime(v, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            raise ValueError("Incorrect date format, should be YYYY-MM-DD HH:MM:SS")
