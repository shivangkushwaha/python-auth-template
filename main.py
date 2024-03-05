from fastapi import FastAPI
from os import listdir
from os.path import isfile, join
import importlib
import uvicorn
from dotenv import load_dotenv
load_dotenv()  # Load variables from .env file
from config.db import MySQLConnector
from api.middleware.common import CustomResponseMiddleware

app = FastAPI(
    title="Tool Market Place",
    description="A Tool Market Place.",
    version="1.0.0"
)
mysql_connector = MySQLConnector()

app.add_middleware(CustomResponseMiddleware)

# Dynamically import all route files from the routes directory
routes_dir = "api/routers"
route_files = [f for f in listdir(routes_dir) if isfile(join(routes_dir, f)) and f.endswith(".py")]

for route_file in route_files:
    module_name = f"api.routers.{route_file[:-3]}"  # Strip ".py" extension
    route_module = importlib.import_module(module_name)
    app.include_router(route_module.router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
