from fastapi import APIRouter,Depends,Request
from api.controller import user as controller
from api.middleware.common import verify_auth_header
# Define Route for the all user request

router = APIRouter(tags=["Users"])

# Apply the middleware to the router
# router.middleware(response_handler)


@router.get("/users")
async def get_users():
    return controller.get_users()

@router.get("/")
async def secure_endpoint(request: Request, _: str = Depends(verify_auth_header)):
    # Access the auth value from the request state
    auth_value = request.state.auth
    return {"message": "Secure endpoint accessed", "auth": auth_value}
