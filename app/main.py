from fastapi import FastAPI


app = FastAPI()

# Include routers here
from routers import image_route, test_route

app.include_router(image_route.router)
app.include_router(test_route.router)

