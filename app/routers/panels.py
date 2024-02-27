"""
This file will have routes for getting and setting panel data, school data, and specialization data. 
"""

# import fastapi stuff
from fastapi import APIRouter, Response, HTTPException
from pymongo.errors import PyMongoError

# import the assistance service
from services.assistanceMongoDB import MongoService

# import models
from models.PanelModels import Panel

router = APIRouter(prefix="/panels", tags=["Panels, Schools and Specializations"])


@router.get("/test", status_code=200, summary="Test route")
def index():
    return Response(content="Hello, World!", status_code=200)


# Add a panel
@router.post("/add_panel", status_code=201, summary="Add a panel")
def add_panel(panel: Panel):
    """
    This route adds a panel to the database.
    : param panel: The panel to be added.
    : return: The added panel.
    """
    try:
        add_panel_service = MongoService()
        added_panel = add_panel_service.add_panel(panel)
        if added_panel:
            return added_panel
        else:
            raise HTTPException(
                status_code=500, detail="An error occurred while adding the panel"
            )
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))


# Get all panels
@router.get("/get_all_panels", status_code=200, summary="Get all panels")
def get_all_panels():
    """
    This route gets all the panels from the database.
    : return: A list of all the panels in the database.
    """
    try:
        get_all_panels_service = MongoService()
        all_panels = get_all_panels_service.get_all_panels()
        if all_panels:
            return all_panels
        else:
            raise HTTPException(
                status_code=500, detail="An error occurred while getting all panels"
            )
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))
