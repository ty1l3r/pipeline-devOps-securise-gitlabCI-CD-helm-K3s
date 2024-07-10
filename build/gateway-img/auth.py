import os
import jwt
import datetime

from exceptions import AuthTokenMissing, AuthTokenExpired, AuthTokenCorrupted
from conf import settings

JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'your_secret_key_here')
ALGORITHM = "HS256"

def decode_access_token(authorization):
    """
    Decode JWT token from authorization header
    """
    if not authorization:
        raise AuthTokenMissing('Authorization header is missing.')
    
    try:
        scheme, token = authorization.split()
        if scheme.lower() != 'bearer':
            raise AuthTokenCorrupted('Invalid token scheme. Use Bearer')
    except ValueError:
        raise AuthTokenCorrupted('Invalid authorization header format.')
        
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise AuthTokenExpired('Token has expired.')
    except jwt.InvalidTokenError:
        raise AuthTokenCorrupted('Invalid token.')

def generate_access_token(data):
    """
    Generate JWT token based on user data
    """
    to_encode = data.copy()
    expire = datetime.datetime.utcnow() + datetime.timedelta(
        minutes=settings.ACCESS_TOKEN_DEFAULT_EXPIRE_MINUTES
    )
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def is_admin_user(token_payload):
    """
    Check if user has admin privileges
    """
    return token_payload.get('user_type') == 'admin'

def is_default_user(token_payload):
    """
    Check if user has default privileges
    """
    return token_payload.get('user_type') in ('default', 'admin')

def generate_request_header(token_payload):
    """
    Generate request headers for service-to-service communication
    """
    return {
        'request_user_id': str(token_payload.get('id')),
        'Content-Type': 'application/json'
    }
