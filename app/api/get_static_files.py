from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter(
	prefix="/static",
	tags=["static"])

@router.get("/{page_name}/{path}/{file_name}")
async def get_static_files(page_name, path, file_name):
	return FileResponse(f"frontend/{page_name}/{path}/{file_name}")