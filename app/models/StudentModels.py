from pydantic import BaseModel
from typing import Optional, List


class StudentModel(BaseModel):
    name: str
    prn: str
    panel: str
    panel_roll_no: int
    face_encoding: Optional[str] = ""
    faces: Optional[List] = []
    # add validators to check if the panels and stuff are actually valid, cache databases if necessary to avoid multiple router calls

    def set_id(self, _id):
        self._id = _id


# this is what should be used to give a response when we ask to get info about a student.
# note that encoding info isnt given here, coz its not necessary, and also, we dont want to give out the encoding info to anyone who asks for it. This is a security measure, and thereby emphasizes the need for Separate Response Models.
class StudentResponseModel(BaseModel):
    _id: str
    name: str
    prn: str
    panel: str
    panel_roll_no: Optional[int] = None


# this is what should be called when getting an encoding for a student face.
# used to store this encoding in firebase. The url is returned of the stored encoding, and is stored in mongodb.
class EncodingModel(BaseModel):
    student_id: str
    no_of_faces: int


class EncodingResponseModel(BaseModel):
    _id: str
    student_id: str
    number_of_faces: int
    encoding_url: str  # this is the firebase url where the encoding is stored.
