from fastapi import FastAPI


app = FastAPI()

# Include routers here
from routers import client_uploads, test_route, face_rec, college, subjects, students, teachers, classes, panels

app.include_router(client_uploads.router)
app.include_router(students.router)
app.include_router(face_rec.router)
app.include_router(panels.router)
app.include_router(college.router)
app.include_router(subjects.router)
app.include_router(teachers.router)
app.include_router(classes.router)
app.include_router(test_route.router)

