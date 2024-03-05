from fastapi import APIRouter
from fastapi import UploadFile, File, Form
from api.controller.tools import create_tools, get_list, get_details
from api.validators.common import ListAPI
# Define Route for the all user request

router = APIRouter(tags=["Tools"])



@router.post("/tool")
async def save_tools(name :str = Form(...) ,description :str = Form(...) ,instruction :str = Form(...) ,capabilities :str = Form(...) ,github_link :str = Form(...) ,run_commands :str = Form(...), conversation_starters:str =Form(...),  file: UploadFile = File(...)):
    """_summary_
        capabilities : list (csv form)
        conversation_starters : list (csv form)
        Returns:
            _type_: _description_
    """
    capabilities = capabilities.split(',')
    conversation_starters = conversation_starters.split(',')
    return create_tools(name, description, instruction, capabilities, github_link, run_commands, conversation_starters, file)


@router.get("/tool")
async def get_tools_list(page: int =1, limit: int =10):
    """_summary_
        Returns:
            _type_: _description_
    """
    return get_list(page, limit)


@router.get("/tool/{id}")
async def get_tools_details(id:int):
    """_summary_
        Returns:
            _type_: _description_
    """
    return get_details(id)



