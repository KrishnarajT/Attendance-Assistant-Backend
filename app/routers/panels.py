"""
This file will have routes for getting and setting panel data, school data, and specialization data.
"""

# import fastapi stuff
from fastapi import APIRouter, Response, HTTPException
from pymongo.errors import PyMongoError

# import models
from models.PanelModels import (
    PanelModel,
    SchoolModel,
    SpecializationModel,
    SpecializationResponseModel,
)

# import services
from services.panel_services import (
    add_panel,
    get_all_panels,
    set_current_sem_for_panel,
    add_semester_to_panel,
    add_student_to_panel,
)

from services.school_and_spec_services import (
    add_school,
    get_all_schools,
    add_specialization,
    get_all_specializations,
    update_school_for_panel,
    update_spec_for_panel,
    add_spec_to_school,
)


router = APIRouter(prefix="/panels", tags=["Panels, Schools and Specializations"])


@router.get("/test", status_code=200, summary="Test route")
def index_route():
    return Response(content="Hello, World!", status_code=200)


# Add a panel
@router.post("/add_panel", status_code=201, summary="Add a panel")
def add_panel_route(panel: PanelModel):
    """
    This route adds a panel to the database.
    : param panel: The panel to be added.
    : return: The added panel.
    """
    try:
        added_panel = add_panel(panel)
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
def get_all_panels_route():
    """
    This route gets all the panels from the database.
    : return: A list of all the panels in the database.
    """
    try:
        all_panels = get_all_panels()
        if all_panels:
            return all_panels
        else:
            raise HTTPException(
                status_code=500, detail="An error occurred while getting all panels"
            )
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/add_school", status_code=201, summary="Add a school")
def add_school_route(school: SchoolModel):
    """
    This route adds a school to the database.
    : param school: The school to be added.
    : return: The added school.
    """
    try:
        added_school = add_school(school)
        if added_school:
            return added_school
        else:
            raise HTTPException(
                status_code=500, detail="An error occurred while adding the school"
            )
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/get_all_schools", status_code=200, summary="Get all schools")
def get_all_schools_route():
    """
    This route gets all the schools from the database.
    : return: A list of all the schools in the database.
    """
    try:
        all_schools = get_all_schools()
        if all_schools:
            return all_schools
        else:
            raise HTTPException(
                status_code=500, detail="An error occurred while getting all schools"
            )
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/add_specialization", status_code=201, summary="Add a specialization")
def add_specialization_route(specialization: SpecializationModel):
    """
    This route adds a specialization to the database.
    : param specialization: The specialization to be added.
    : return: The added specialization.
    """
    try:
        added_specialization = add_specialization(specialization)
        if not added_specialization:
            raise HTTPException(
                status_code=500,
                detail="An error occurred while adding the specialization",
            )
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))

    return SpecializationResponseModel(
        _id=added_specialization._id,
        name=added_specialization.name,
        panels=added_specialization.panels,
    )


@router.get(
    "/get_all_specializations", status_code=200, summary="Get all specializations"
)
def get_all_specializations_route():
    """
    This route gets all the specializations from the database.
    : return: A list of all the specializations in the database.
    """
    try:
        all_specializations = get_all_specializations()
        if not all_specializations:
            raise HTTPException(
                status_code=500,
                detail="An error occurred while getting all specializations",
            )
        return all_specializations
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post(
    "/add_spec_to_school", status_code=201, summary="Add a specialization to a school"
)
def add_spec_to_school_route(school_id: str, spec_id: str):
    """
    This route adds a specialization to a school.
    : param school_id: The school to which the specialization is to be added.
    : param spec_id: The specialization to be added to the school.
    : return: The updated school.
    """
    try:
        updated_school = add_spec_to_school(school_id, spec_id)
        if updated_school:
            return updated_school
        else:
            raise HTTPException(
                status_code=500,
                detail="An error occurred while adding the specialization to the school",
            )
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post(
    "/update_school_for_panel", status_code=201, summary="Update school for a panel"
)
def update_school_for_panel_route(panel_id: str, school_id: str):
    """
    This route updates the school for a panel.
    : param panel_id: The panel for which the school is to be updated.
    : param school_id: The school to be updated for the panel.
    : return: The updated panel.
    """
    try:
        updated_panel = update_school_for_panel(panel_id, school_id)
        if updated_panel:
            return updated_panel
        else:
            raise HTTPException(
                status_code=500,
                detail="An error occurred while updating the school for the panel",
            )
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post(
    "/update_spec_for_panel",
    status_code=201,
    summary="Update specialization for a panel",
)
def update_spec_for_panel_route(panel_id: str, spec_id: str):
    """
    This route updates the specialization for a panel.
    : param panel_id: The panel for which the specialization is to be updated.
    : param spec_id: The specialization to be updated for the panel.
    : return: The updated panel.
    """
    try:
        updated_panel = update_spec_for_panel(panel_id, spec_id)
        if updated_panel:
            return updated_panel
        else:
            raise HTTPException(
                status_code=500,
                detail="An error occurred while updating the specialization for the panel",
            )
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post(
    "/set_current_sem_for_panel",
    status_code=201,
    summary="Set current semester for a panel",
)
def set_current_sem_for_panel_route(panel_id: str, sem_id: str):
    """
    This route sets the current semester for a panel.
    : param panel_id: The panel for which the current semester is to be set.
    : param sem_id: The semester to be set as the current semester for the panel.
    : return: The updated panel.
    """
    try:
        updated_panel = set_current_sem_for_panel(panel_id, sem_id)
        if updated_panel:
            return updated_panel
        else:
            raise HTTPException(
                status_code=500,
                detail="An error occurred while setting the current semester for the panel",
            )
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post(
    "/add_semester_to_panel", status_code=201, summary="Add a semester to a panel"
)
def add_semester_to_panel_route(panel_id: str, sem_id: str):
    """
    This route adds a semester to a panel.
    : param panel_id: The panel to which the semester is to be added.
    : param sem_id: The semester to be added to the panel.
    : return: The updated panel.
    """
    try:
        updated_panel = add_semester_to_panel(panel_id, sem_id)
        if updated_panel:
            return updated_panel
        else:
            raise HTTPException(
                status_code=500,
                detail="An error occurred while adding the semester to the panel",
            )
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post(
    "/add_student_to_panel", status_code=201, summary="Add a student to a panel"
)
def add_student_to_panel_route(panel_id: str, student_id: str):
    """
    This route adds a student to a panel.
    : param panel_id: The panel to which the student is to be added.
    : param student_id: The student to be added to the panel.
    : return: The updated panel.
    """
    try:
        add_student_to_panel(panel_id, student_id)
        return True
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))
