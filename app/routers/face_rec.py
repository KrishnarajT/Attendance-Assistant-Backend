'''
This file contains the routes for interaction with any face recognition models, or actually carrying out the face recognition process.
'''


from fastapi import APIRouter

router = APIRouter(prefix="/face_rec", tags=["Face Recognition"])