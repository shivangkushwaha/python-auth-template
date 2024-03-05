from fastapi.responses import JSONResponse
from api.handlers.helper import calculate_limit_offset,calculate_total_pages
from api.models.tool import Tool
import uuid
import os
import shutil
import json


def create_tools(name :str ,description :str ,instruction :str ,capabilities :list ,github_link :str ,run_commands :str, conversation_starters: list,  file):
    try:
        # Create a directory to store uploaded files if it doesn't exist
        os.makedirs("uploads", exist_ok = True)
        generated_uuid = str(uuid.uuid4())
        _, file_extension = os.path.splitext(file.filename)
        filename = generated_uuid + file_extension
        
        # Save the uploaded file to the uploads directory
        with open(os.path.join("uploads", filename), "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        save_data = {
            "name":file.filename,
            "size":file.spool_max_size,
            "type":file.content_type,
            "path":os.path.join("uploads", filename)
        }
        
        #  Setting Up Json Data
        conversation_starters = json.dumps(conversation_starters)
        capabilities = json.dumps(capabilities)
        
        # create tool with provided data
        results = Tool.create(name, description, instruction, 
        capabilities, github_link, run_commands, 
        conversation_starters,file_path = save_data['path'],
        file_size = save_data['size'],content_type = save_data['type'],
        file_extension = file_extension, uuid = generated_uuid)
        
        if results == 1:
            return JSONResponse(content = {"message": "File uploaded successfully", "data": save_data}, status_code = 200)
        else:
            return JSONResponse(content = {"message": "Something Seems Bad", "file_name": {}}, status_code = 400)
    except Exception as e:
        return JSONResponse(content={"message": f"Failed to upload file: {e}"}, status_code = 500)
        

def get_list(page,limit):
    try:
        limit, offset = calculate_limit_offset(page, limit)
        records,total_records = Tool.list(limit, offset)
        total_pages = calculate_total_pages(total_records['count'], limit)
        returnData = {
            "current_page": page,
            "limit": limit,
            "records": records,
            "total_pages": total_pages
        }
        return JSONResponse(content={"message": "Records fetched successfully.", "data": returnData }, status_code = 200)    
    except Exception as e:
        return JSONResponse(content={"message": f"Failed to get list for tools: {e}"}, status_code = 500)


def get_details(id: int):
    try:
        tool = Tool.details(id)
        if tool:
            return JSONResponse(content = {"message": "Records fetched successfully.", "data": tool }, status_code = 200)
        else: 
            return JSONResponse(content = {"message": "Invalid id Provided.", "data": {} }, status_code = 400)

    except Exception as e:
        return JSONResponse(content={"message": f"Failed to get list for tools: {e}"}, status_code = 500)