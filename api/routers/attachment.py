from fastapi import APIRouter
from api.controller.attachment import getFile

router = APIRouter(tags=["Attachment"])


@router.get("/file")
async def list_files(path: str):
    return getFile(path)
