from jose import jwt,JWTError
from datetime import datetime, timedelta
import math
import os

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
DEFAULT_EXPIRE_TIME = os.getenv("DEFAULT_EXPIRE_TIME")

def calculate_limit_offset(page_number, limit):
    """
    Calculate limit and offset based on page number and limit.
    
    Args:
        page_number (int): Page number (starting from 1).
        limit (int): Number of items per page.
    
    Returns:
        tuple: A tuple containing limit and offset.
    """
    # Ensure page number is positive
    page_number = max(1, page_number)

    # Calculate offset
    offset = (page_number - 1) * limit
    
    # Return limit and offset
    return limit, offset

def calculate_total_pages(total_records, limit):
    """
    Calculate total number of pages based on total number of records and limit.
    
    Args:
        total_records (int): Total number of records.
        limit (int): Number of items per page.
    
    Returns:
        int: Total number of pages.
    """
    # Calculate total number of pages
    total_pages = math.ceil(total_records / limit)
    
    # Return total number of pages 
    return total_pages

def create_jwt_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta( days = DEFAULT_EXPIRE_TIME)  # Default expiration time
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)
    return encoded_jwt

def verify_jwt_token(token: str):
    try:
        # Decode the token and validate its signature and expiration
        payload = jwt.decode(token, SECRET_KEY, algorithms = [ALGORITHM])
        return payload  # Return the original payload data
    except jwt.ExpiredSignatureError:
        raise Exception("Token has expired")
    except JWTError:
        raise Exception("Token is invalid")