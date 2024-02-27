"""
This file will have routes for getting and setting panel data, school data, and specialization data. 
"""

# import fastapi stuff
from fastapi import APIRouter, Response, HTTPException
from pymongo.errors import PyMongoError

# import the assistance service
from services.assistanceMongoDB import MongoService

# import models
from models.PanelModels import PanelModel, SchoolModel, SpecializationModel, SemesterModel

router = APIRouter(prefix="/panels", tags=["Panels, Schools and Specializations"])


@router.get("/test", status_code=200, summary="Test route")
def index():
    return Response(content="Hello, World!", status_code=200)


# Add a panel
@router.post("/add_panel", status_code=201, summary="Add a panel")
def add_panel(panel: PanelModel):
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

@router.post("/add_school", status_code=201, summary="Add a school")
def add_school(school: SchoolModel):
    """
    This route adds a school to the database.
    : param school: The school to be added.
    : return: The added school.
    """
    try:
        add_school_service = MongoService()
        added_school = add_school_service.add_school(school)
        if added_school:
            return added_school
        else:
            raise HTTPException(
                status_code=500, detail="An error occurred while adding the school"
            )
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/get_all_schools", status_code=200, summary="Get all schools")
def get_all_schools():
    """
    This route gets all the schools from the database.
    : return: A list of all the schools in the database.
    """
    try:
        get_all_schools_service = MongoService()
        all_schools = get_all_schools_service.get_all_schools()
        if all_schools:
            return all_schools
        else:
            raise HTTPException(
                status_code=500, detail="An error occurred while getting all schools"
            )
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/add_specialization", status_code=201, summary="Add a specialization")
def add_specialization(specialization: SpecializationModel):
    """
    This route adds a specialization to the database.
    : param specialization: The specialization to be added.
    : return: The added specialization.
    """
    try:
        add_specialization_service = MongoService()
        added_specialization = add_specialization_service.add_specialization(specialization)
        if added_specialization:
            return added_specialization
        else:
            raise HTTPException(
                status_code=500, detail="An error occurred while adding the specialization"
            )
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/get_all_specializations", status_code=200, summary="Get all specializations")
def get_all_specializations():
    """
    This route gets all the specializations from the database.
    : return: A list of all the specializations in the database.
    """
    try:
        get_all_specializations_service = MongoService()
        all_specializations = get_all_specializations_service.get_all_specializations()
        if all_specializations:
            return all_specializations
        else:
            raise HTTPException(
                status_code=500, detail="An error occurred while getting all specializations"
            )
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/add_spec_to_school", status_code=201, summary="Add a specialization to a school")
def add_spec_to_school(school_id: str, spec_id: str):
    """
    This route adds a specialization to a school.
    : param school_id: The school to which the specialization is to be added.
    : param spec_id: The specialization to be added to the school.
    : return: The updated school.
    """
    try:
        add_spec_to_school_service = MongoService()
        updated_school = add_spec_to_school_service.add_spec_to_school(school_id, spec_id)
        if updated_school:
            return updated_school
        else:
            raise HTTPException(
                status_code=500, detail="An error occurred while adding the specialization to the school"
            )
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.post("/update_school_for_panel", status_code=201, summary="Update school for a panel")
def update_school_for_panel(panel_id: str, school_id: str):
    """
    This route updates the school for a panel.
    : param panel_id: The panel for which the school is to be updated.
    : param school_id: The school to be updated for the panel.
    : return: The updated panel.
    """
    try:
        update_school_for_panel_service = MongoService()
        updated_panel = update_school_for_panel_service.update_school_for_panel(panel_id, school_id)
        if updated_panel:
            return updated_panel
        else:
            raise HTTPException(
                status_code=500, detail="An error occurred while updating the school for the panel"
            )
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/update_spec_for_panel", status_code=201, summary="Update specialization for a panel")
def update_spec_for_panel(panel_id: str, spec_id: str):
    """
    This route updates the specialization for a panel.
    : param panel_id: The panel for which the specialization is to be updated.
    : param spec_id: The specialization to be updated for the panel.
    : return: The updated panel.
    """
    try:
        update_spec_for_panel_service = MongoService()
        updated_panel = update_spec_for_panel_service.update_spec_for_panel(panel_id, spec_id)
        if updated_panel:
            return updated_panel
        else:
            raise HTTPException(
                status_code=500, detail="An error occurred while updating the specialization for the panel"
            )
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set_current_sem_for_panel", status_code=201, summary="Set current semester for a panel")
def set_current_sem_for_panel(panel_id: str, sem_id: str):
    """
    This route sets the current semester for a panel.
    : param panel_id: The panel for which the current semester is to be set.
    : param sem_id: The semester to be set as the current semester for the panel.
    : return: The updated panel.
    """
    try:
        set_current_sem_for_panel_service = MongoService()
        updated_panel = set_current_sem_for_panel_service.set_current_sem_for_panel(panel_id, sem_id)
        if updated_panel:
            return updated_panel
        else:
            raise HTTPException(
                status_code=500, detail="An error occurred while setting the current semester for the panel"
            )
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/add_semester_to_panel", status_code=201, summary="Add a semester to a panel")
def add_semester_to_panel(panel_id: str, sem_id: str):
    """
    This route adds a semester to a panel.
    : param panel_id: The panel to which the semester is to be added.
    : param sem_id: The semester to be added to the panel.
    : return: The updated panel.
    """
    try:
        add_semester_to_panel_service = MongoService()
        updated_panel = add_semester_to_panel_service.add_semester_to_panel(panel_id, sem_id)
        if updated_panel:
            return updated_panel
        else:
            raise HTTPException(
                status_code=500, detail="An error occurred while adding the semester to the panel"
            )
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))