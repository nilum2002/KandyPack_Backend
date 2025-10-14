import os
from datetime import datetime, timedelta
from typing import Union, Dict
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core import model  # uses your model.Users

# Config (use environment variables in production)
SECRET_KEY = os.getenv("KANDYPACK_SECRET_KEY", "dev-secret-change-me")
ALGORITHM = os.getenv("KANDYPACK_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("KANDYPACK_ACCESS_TOKEN_EXPIRE_MINUTES", "60"))
# app/core/auth.py
import os
from datetime import datetime, timedelta
from typing import Union, Dict
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core import model  # uses your model.Users

# Config (use environment variables in production)
SECRET_KEY = os.getenv("KANDYPACK_SECRET_KEY", "dev-secret-change-me")
ALGORITHM = os.getenv("KANDYPACK_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("KANDYPACK_ACCESS_TOKEN_EXPIRE_MINUTES", "60"))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")  # ensure login uses this path

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")  # ensure login uses this path

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

import os
from datetime import datetime, timedelta
from typing import Union, Dict
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core import model

# Security configuration (use env vars in production)
SECRET_KEY = os.getenv("KANDYPACK_SECRET_KEY", "dev-secret-change-me")
ALGORITHM = os.getenv("KANDYPACK_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("KANDYPACK_ACCESS_TOKEN_EXPIRE_MINUTES", "60"))

# Password hashing and OAuth2 scheme
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain password against a hashed password"""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """Generate a hash from a plain password"""
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None) -> str:
    """Create a JWT access token"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def _get_user_by_id(db: Session, user_id: str):
    return db.query(model.Users).filter(model.Users.user_id == user_id).first()

async def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)) -> Dict:
    """Get the current authenticated user from the JWT token"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = _get_user_by_id(db, user_id)
    if user is None:
        raise credentials_exception

    return {"user_id": user.user_id, "username": user.user_name, "role": user.role}

def require_management(current_user: Dict = Depends(get_current_user)) -> Dict:
    """Dependency that ensures the current user has role 'Management'"""
    if not current_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    role = (current_user.get("role") or "").strip()
    if role != "Management":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Management role required")
    return current_user