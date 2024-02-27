from pydantic import BaseModel
from typing import Optional, List

# {
#   "_id": "Panel ID Generated by MongoDB",
#   "panel_letter": "A",
#   "school": "School ID",
#   "specialization": "Specialization ID",
#   "students": [
#     "Student ID 1",
#     "Student ID 2"
#   ],
#   "semesters": [
#     "Semester ID 1",
#     "Semester ID 2"
#   ],
#   "current_semester": "Semester ID"
# }


class Panel(BaseModel):
    panel_letter: str
    school: str
    specialization: str
    students: List[str]
    semesters: List[str]
    current_semester: str


class PanelID(BaseModel):
    panel_id: str
