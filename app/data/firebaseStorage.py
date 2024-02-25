# This file is used to initialize the firebase storage and return the storage object
import firebase_admin
from firebase_admin import credentials, storage

cred = credentials.Certificate("attendance-assistant-3b3a3-firebase-adminsdk-vkifz-64ed71fe03.json")
firebase_admin.initialize_app(cred)

fb_storage = storage.bucket("attendance-assistant-3b3a3.appspot.com")