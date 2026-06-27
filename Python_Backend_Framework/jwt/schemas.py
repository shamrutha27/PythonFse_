from pydantic import BaseModel, EmailStr
from typing import Optional, List


# ======================================================
# COURSE SCHEMAS
# ======================================================

class CourseBase(BaseModel):
    code: str
    name: str
    instructor: str


class CourseCreate(CourseBase):
    pass


class CourseUpdate(BaseModel):
    code: Optional[str] = None
    name: Optional[str] = None
    instructor: Optional[str] = None


class CourseResponse(CourseBase):
    id: int

    class Config:
        from_attributes = True


# Pagination Schema (Hands-On 8)
class PaginatedCourses(BaseModel):
    count: int
    next: Optional[str] = None
    previous: Optional[str] = None
    results: List[CourseResponse]


# ======================================================
# USER SCHEMAS
# ======================================================

# User Registration
class UserRegister(BaseModel):
    email: EmailStr
    password: str


# User Login
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# Response after Registration
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    class Config:
        from_attributes = True


# ======================================================
# JWT TOKEN SCHEMAS
# ======================================================

# Returned after successful login
class Token(BaseModel):
    access_token: str
    token_type: str


# Token Payload
class TokenData(BaseModel):
    email: Optional[str] = None