from fastapi import APIRouter
from api.validators.metadata import MetaData
from api.controller.attachment import getFile
from api.controller.metadata import save_metadata
router = APIRouter( tags = ["Metadata"] )


@router.post("/metadata")
async def create_metadata(data: MetaData):
    return save_metadata(data)
