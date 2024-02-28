from fastapi import FastAPI
# from fastapi.responses import JSONResponse
# from db import models
# from db.db import engine
# from fastapi import HTTPException
# from fastapi import status
# from routers.routes import user_routes
# from routers.routes import article_routes
# from exceptions import StoryException
# from routers.routes import product_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# app.include_router(user_routes.router)
# app.include_router(article_routes.router)
# app.include_router(product_routes.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/hello")
def index():
    return {"message": "Hello World"}
