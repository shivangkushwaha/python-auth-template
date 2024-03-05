from fastapi import Request, HTTPException, Header, Depends
from starlette.middleware.base import BaseHTTPMiddleware

async def verify_auth_header(request: Request, auth: str = Header(None)):
    if auth is None:
        # Raise an HTTPException with a 401 status code indicating unauthorized access
        raise HTTPException(status_code=401, detail = {} )
    # Attach the auth header value to the request's state for later use in the endpoint
    request.state.auth = auth


# middleware.py

class CustomResponseMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        """
        This custom middleware adds response and status code based on last function call 
        """
        print("response",response)
        response.headers['X-Custom-Header'] = 'Value'  # Modify the response
        return response
