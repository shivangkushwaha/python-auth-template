import os
from fastapi.responses import JSONResponse
from api.validators.metadata import MetaData 
from api.models.metadata import MetaData as MetaDataModel

def save_metadata(data:MetaData):
    try:
        res = MetaDataModel.create(data.tool_id, data.score, data.metadata)
        print(res)
        if res:
            return JSONResponse(content={"message": "Records fetched successfully.", "data": {} }, status_code = 200)
        else: 
            return JSONResponse(content={"message": "Something Wrong.", "data": {} }, status_code = 400)

    except Exception as e:
        return JSONResponse(content={"message": f"Failed to save metadata : {e}"}, status_code = 500)