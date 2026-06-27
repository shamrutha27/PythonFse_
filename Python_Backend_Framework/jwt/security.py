from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

import models
from database import SessionLocal

# ======================================================
# JWT Configuration
# ======================================================

SECRET_KEY = "your_secret_key_here_change_this"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# ======================================================
# Password Hashing (bcrypt)
# ======================================================

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 token URL
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


# ======================================================
# Database Dependency
# ======================================================

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ======================================================
# Password Utilities
# ======================================================

# bcrypt is intentionally slow, making brute-force attacks
# much harder than MD5 or SHA-256, which are designed to be fast.
# Never store plain-text passwords.

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


# ======================================================
# JWT Token Creation
# ======================================================

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt


# ======================================================
# Get Current User
# ======================================================

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or expired token",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        email = payload.get("sub")

        if email is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    user = db.query(models.User).filter(
        models.User.email == email
    ).first()

    if user is None:
        raise credentials_exception

    return user