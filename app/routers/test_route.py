from fastapi import APIRouter, status, Response

router = APIRouter()


@router.get("/test", status_code=status.HTTP_200_OK, tags=["test"], summary="Test route")
def index():
	return Response(status_code=200, content="Hello, World!")
