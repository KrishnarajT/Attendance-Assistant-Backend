from fastapi import FastAPI


app = FastAPI()

# Include routers here
from routers import client_uploads, test_route

app.include_router(client_uploads.router)
app.include_router(test_route.router)

