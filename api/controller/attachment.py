import os
from fastapi.responses import JSONResponse, FileResponse


def getFile(path: str):
    file_path = os.getcwd() + f"/{path}"
    print('file_path',file_path)
    # Check if the file exists
    if os.path.isfile(file_path):
        # Get file information
        return FileResponse(file_path)
    else:
        return {"error": "File not found"}