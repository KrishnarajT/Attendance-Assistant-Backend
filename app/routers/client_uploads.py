"""
This file contains the routes for uploading images and attendance information from the client side. So that means any route that sends data, and doesnt expect any data other than urls, from app or phones or websites, should be here. Not all functions are written for api use only, some can be called from the server side as well.
"""

from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse, Response
from services.assistanceFirebase import AssistanceFirebase
from datetime import datetime
from services.lecture_services import get_lecture_images_between_time_on_date

from facial_recognition.StudentManager import StudentManager
from facial_recognition.FaceRec import FaceRec

# import models
from models.ClientUploadModels import (
    AddFaceModel,
    AddFaceResponseModel,
    AddClassPhotoModel,
    AddClassPhotoResponseModel,
    FaceEncodingModel,
    FaceEncodingResponseModel,
    AttendanceModel,
)


# import services
from services.panel_services import (
    get_student_encodings_from_panel_id,
    get_current_sem_from_panel,
)

from services.student_services import (
    add_student_face_to_db,
    add_student_encoding,
)

from services.lecture_services import add_class_photo_to_db, add_lecture

fb_storage = AssistanceFirebase()

router = APIRouter(
    prefix="/upload", tags=["Upload Images or Attendance Info from App/Website/Pi"]
)


@router.post("/add_student_face_from_url", response_model=AddFaceResponseModel)
async def add_student_face_from_url_route(student_id: int, face_image_url: str):
    """
    Adds a face to the student's row in the student collection in the database. This is going to be one of the base faces of the student, from which the model trains.

    :return: URL of the uploaded image.
    """
    try:
        # add this face to the student's row in student collection in the database.
        await add_student_face_to_db(face_image_url, student_id)
    except Exception as e:
        return Response(
            status_code=500,
            content={
                "detail": f"An error occurred while adding face to database: {str(e)}"
            },
        )

    # to return information about the face that was added, we create a new object of the AddFaceModel class,
    # and return that object. these attributes may change.
    output_face_model = AddFaceResponseModel(
        student_id=student_id, face_image_url=face_image_url
    )
    return Response(status_code=200, content=output_face_model)


@router.post("/add_student_face", response_model=AddFaceResponseModel)
async def add_student_face_route(student_id: str, face_image: UploadFile = File(...)):
    """
    Uploads face image to firebase. This is going to be one of the base faces of the student, from which the model trains.
    :return: URL of the uploaded image.
    """
    # read image
    face_image = await face_image.read()
    add_face_model = AddFaceModel(student_id=student_id, face_image=face_image)
    # upload image to firebase
    try:
        face_image_url = fb_storage.upload_image(face_image)
    except Exception as e:
        print(e)
        return JSONResponse(
            status_code=500,
            content={"detail": f"An error occurred while uploading image: {str(e)}"},
        )

    # add the face to the student's row in the student collection in mongodb.
    try:
        # add this face to the student's row in student collection in the database.
        add_student_face_to_db(student_id, face_image_url)
    except Exception as e:
        return Response(
            status_code=500,
            content={
                "detail": f"Uploaded Image {face_image_url}, but An error occurred while adding face to database: {str(e)}"
            },
        )

    # to return information about the face that was added, we create a new object of the AddFaceModel class,
    # and return that object.
    output_face_model = AddFaceResponseModel(
        student_id=add_face_model.student_id, face_image_url=face_image_url
    )
    return output_face_model


@router.post("/add_class_photo_from_url", response_model=AddClassPhotoResponseModel)
async def add_class_photo_from_url_route(room_id, date, time, class_photo_url: str):
    """
    Adds class photo to firebase. This is ideally from PI. Non ideally from teachers phone.
    :return: URL of the uploaded image.
    """
    add_class_photo_model = AddClassPhotoModel(room_id=room_id, date=date, time=time)
    # create a new row in the Lecture Images collection in the database, with the class_id, room_id, date, time,
    # class_photo_url
    try:
        # add this face to the student's row in student collection in the database.
        add_class_photo_to_db(
            add_class_photo_model.room_id,
            add_class_photo_model.date,
            add_class_photo_model.time,
            class_photo_url,
        )
    except Exception as e:
        return Response(
            status_code=500,
            content={
                "detail": f"Uploaded Image {class_photo_url}, but An error occurred while adding pic to database: {str(e)}"
            },
        )

    # to return information about the class photo that was added, we create a new object of the AddClassPhotoModel
    # class, and return that object.
    output_class_photo = AddClassPhotoResponseModel(
        add_class_photo_model.room_id,
        add_class_photo_model.date,
        add_class_photo_model.time,
        class_photo_url=class_photo_url,
    )
    return output_class_photo


@router.post("/add_class_photo", response_model=AddClassPhotoResponseModel)
async def add_class_photo_route(
    room_id,
    date,
    time,
    class_photo: UploadFile = File(...),
):
    """
    Adds class photo to firebase. This is ideally from PI. Non ideally from teachers phone.
    :return: URL of the uploaded image.
    """
    add_class_photo_model = AddClassPhotoModel(room_id=room_id, date=date, time=time)

    # read image
    class_photo = await class_photo.read()

    # upload image to firebase
    try:
        class_photo_url = fb_storage.upload_image(class_photo)
    except Exception as e:
        return Response(
            status_code=500,
            content={"detail": f"An error occurred while uploading image: {str(e)}"},
        )

    # create a new row in the Lecture Images collection in the database, with the class_id, room_id, date, time,
    # class_photo_url

    # add the face to the student's row in the student collection in mongodb.
    try:
        # add this face to the student's row in student collection in the database.
        add_class_photo_to_db(
            add_class_photo_model.room_id,
            add_class_photo_model.date,
            add_class_photo_model.time,
            class_photo_url,
        )
    except Exception as e:
        return Response(
            status_code=500,
            content={
                "detail": f"Uploaded Image {class_photo_url}, but An error occurred while adding pic to database: {str(e)}"
            },
        )

    # to return information about the class photo that was added, we create a new object of the AddClassPhotoModel
    # class, and return that object.
    output_class_photo = AddClassPhotoResponseModel(
        room_id=add_class_photo_model.room_id,
        date=add_class_photo_model.date,
        time=add_class_photo_model.time,
        class_photo_url=class_photo_url,
    )
    return output_class_photo


@router.post("/add_attendance")
async def add_attendance_route(attModel: AttendanceModel):
    """
    Adds attendance to the database. This is information from the teachers' app from the teacher.
    :param attModel: Attendance model that contains all the necessary information
    :return: URL of the uploaded image.
    """
    # add attendance to the database using the attModel object

    # ideally this must be done to the Classes collection, which will have other data from other sources. A new row in the classes collection will be created in this function. Attendance data will be added later to it. This means that only after the teacher manually adds info about which room they are in, and which panel they are teaching, will the processing start. Images however will be stored in advance during the class. This function would ideally be called after the class is over.

    # to return information about the attendance that was added, we create a new object of the AttendanceModel class, and return that object.

    # get the lecture images and student encodings from the database

    # get all lecture images in between the start and end time
    # instantiate lecture
    print(attModel.start_time, attModel.end_time)
    print(attModel.panel, attModel.room)

    # check start time format
    try:
        datetime.strptime(attModel.start_time, "%H:%M")
    except ValueError:
        return {"error": "Incorrect start time format, should be HH:MM"}

    # check end time format
    try:
        datetime.strptime(attModel.end_time, "%H:%M")
    except ValueError:
        return {"error": "Incorrect start time format, should be HH:MM"}

    # check date format
    try:
        datetime.strptime(attModel.date, "%Y-%m-%d")
    except ValueError:
        return {"error": "Incorrect date format, should be YYYY-MM-DD"}

    # print(attModel.lecture_id)
    lecture_images = get_lecture_images_between_time_on_date(
        attModel.start_time, attModel.end_time, attModel.date
    )

    print(lecture_images)
    if not lecture_images:
        return Response(
            status_code=500,
            content={"detail": f"No images found for the given time range"},
        )

    # return lecture_images

    # get all encodings of students in the panel but print error if even one student doesnt have faces. if any student has faces, but no encodings, then create encodings.

    student_encodings, student_faces, no_faces = get_student_encodings_from_panel_id(
        attModel.panel
    )
    print("student_encodings", student_encodings)
    print("student_faces", student_faces)
    print("no_faces", no_faces)
    if len(no_faces) > 0:
        print("These students do not have faces: ", no_faces)
        # return an error, that these students do not have faces.
        # return JSONResponse(
        #     status_code=500,
        #     content={"detail": f"Students {no_faces} do not have faces."}
        # )

    # remove no faces students from the student_encodings dict
    for i in no_faces:
        student_encodings.pop(i)

    student_ids = list(student_encodings.keys())

    # iterate through all encodings, and if they are empty, create an instance of the student manager class, and pass the faces.
    for i, j in student_encodings.items():
        if not j:
            print("Creating encoding for student: ", i)
            student_manager = StudentManager(i, student_faces[i], [])
            # get the encoding from the studentmanager class' create_encoding method.
            student_manager.create_face_encoding()
            # get face encodings from the student manager class
            face_encoding = student_manager.get_serialized_student_face_encodings()
            print(face_encoding)
            # return []
            await add_student_encoding(i, len(student_faces[i]), face_encoding)

    # everything working till here. ------------------
    # call the get attendance function from the face rec class, and pass the needed things.
    face_rec = FaceRec(
        student_encodings,
        lecture_images,
        attModel.panel,
        student_ids,
        attModel.room,
    )
    # get present and absent students from the attendance function. (id)
    present, absent = face_rec.find_attendance()
    print(present, absent)
    # add the no faces people to the absent list.
    absent.extend(no_faces)
    # create a new row in the lectures collection in the database, with the class_id, room_id, date, time, students_present, students_absent, and lecture_images, and teacher and subject id.
    current_semester = get_current_sem_from_panel(attModel.panel)
    new_lecture = {
        "date": attModel.date,
        "start_time": attModel.start_time,
        "end_time": attModel.end_time,
        "subject": attModel.subject,
        "teacher": attModel.teacher,
        "panel": attModel.panel,
        "room": attModel.room,
        "semester": current_semester,
        "students_present": present,
        "students_absent": absent,
        "lecture_images": lecture_images,
    }
    print(new_lecture)
    lec_id = add_lecture(new_lecture)
    if not lec_id:
        return JSONResponse(
            status_code=500,
            content={
                "detail": f"An error occurred while adding the lecture to the database"
            },
        )
    return JSONResponse(
        status_code=200,
        content={
            "detail": f"Lecture added successfully. Present: {present}, Absent: {absent}. id is: {lec_id}"
        },
    )

# separating out this funciton to be called from within the server later on without triggering route.
async def add_face_encoding(student_id: str, number_of_faces: int, face_encoding):
    """
    Adds face encoding to the database. This is done from the server, but a function is written here nonetheless to atomise the process. They are pickle files.
    :param face_encoding_model: Face encoding model that contains all the necessary information
    :return: URL of the uploaded image.
    """
    face_encoding_model = FaceEncodingModel(
        student_id=student_id, number_of_faces=number_of_faces, encoding=face_encoding
    )

    # upload to firebase
    try:
        face_encoding_model_url = fb_storage.upload_encoding(face_encoding)
    except Exception as e:
        return Response(
            status_code=500,
            content={"detail": f"An error occurred while uploading image: {str(e)}"},
        )

    # add face_encoding_model_url to the database using the face_encoding_model object to the students collection.

    # to return information about the face encoding that was added, we create a new object of the FaceEncodingModel class, and return that object.
    # these attributes may change.
    output_face_encoding = FaceEncodingResponseModel(
        student_id=face_encoding_model.student_id,
        number_of_faces=face_encoding_model.number_of_faces,
        encoding_url=face_encoding_model_url,
    )
    return Response(status_code=200, content=output_face_encoding)


@router.post("/add_face_encoding", response_model=FaceEncodingModel)
async def add_face_encoding_route(
    student_id: str, number_of_faces: int, face_encoding: UploadFile = File(...)
):
    face_encoding = await face_encoding.read()
    return await add_face_encoding(student_id, number_of_faces, face_encoding)


@router.post("/update_face_encoding", response_model=FaceEncodingResponseModel)
async def update_face_encoding_route(
    old_encoding_url: str,
    student_id: str,
    number_of_faces: int,
    face_encoding: UploadFile = File(...),
):
    """
    Updates face encoding in the database. This should also be done from the server, but we cant overwrite or update
    files in firebase or s3, so we delete the previous file, and we upload the new file, also changing the url in the
    database, specifically in the student collection. :param old_encoding_url: URL of the old face encoding	:param
    face_encoding_model:  model that contains all the necessary information :return: URL of the uploaded image.
    """
    face_encoding = await face_encoding.read()
    face_encoding_model = FaceEncodingModel(
        student_id=student_id, number_of_faces=number_of_faces, encoding=face_encoding
    )

    # upload the new face encoding to firebase, and get the new url
    try:
        new_face_encoding_url = fb_storage.upload_image(face_encoding)
    except Exception as e:
        return Response(
            status_code=500,
            content={"detail": f"An error occurred while uploading image: {str(e)}"},
        )

    # delete the previous face encoding from firebase
    try:
        fb_storage.delete_image(old_encoding_url)
    except Exception as e:
        return Response(
            status_code=500,
            content={
                "detail": f"An error occurred while deleting previous image: {str(e)}"
            },
        )

    # update face encoding in the database using the face_encoding_model object
    # !! update the url in the student collection

    # to return information about the face encoding that was added, we create a new object of the FaceEncodingModel
    # class, and return that object. these attributes may change.
    output_face_encoding = FaceEncodingResponseModel(
        student_id=face_encoding_model.student_id,
        number_of_faces=face_encoding_model.number_of_faces,
        encoding_url=new_face_encoding_url,
    )

    return Response(status_code=200, content=output_face_encoding)
