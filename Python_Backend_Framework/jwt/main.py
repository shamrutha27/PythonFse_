from fastapi import FastAPI, Depends, HTTPException, status, Response, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

import models
import schemas

from database import SessionLocal, engine
from security import (
    get_password_hash,
    verify_password,
    create_access_token,
    get_current_user
)

# Create Database Tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Course Management API",
    version="1.0"
)

# ----------------------------------------------------
# CORS Configuration
# ----------------------------------------------------
# Allows requests from React frontend running on localhost:3000
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------------------------------
# Database Dependency
# ----------------------------------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ----------------------------------------------------
# Standard Error Response
# ----------------------------------------------------
def error_response(status_code, code, message, field=None):
    return JSONResponse(
        status_code=status_code,
        content={
            "error": {
                "code": code,
                "message": message,
                "field": field
            }
        }
    )


# ----------------------------------------------------
# USER REGISTRATION
# ----------------------------------------------------
@app.post(
    "/api/v1/auth/register/",
    response_model=schemas.UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register_user(
    user: schemas.UserRegister,
    db: Session = Depends(get_db)
):

    existing_user = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

    if existing_user:
        return error_response(
            409,
            "EMAIL_EXISTS",
            "Email is already registered"
        )

    # bcrypt is intentionally slow, making brute-force attacks
    # much harder than MD5 or SHA-256.
    # Never store plain-text passwords.

    hashed_password = get_password_hash(user.password)

    new_user = models.User(
        email=user.email,
        hashed_password=hashed_password,
        is_active=True
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# ----------------------------------------------------
# USER LOGIN
# ----------------------------------------------------
@app.post(
    "/api/v1/auth/login/",
    response_model=schemas.Token
)
def login(
    user: schemas.UserLogin,
    db: Session = Depends(get_db)
):

    db_user = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    if not verify_password(
        user.password,
        db_user.hashed_password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        data={
            "sub": db_user.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# ----------------------------------------------------
# OAuth2 Authorization Code Flow
# ----------------------------------------------------
#
# OAuth2 Authorization Code Flow:
#
# The user authenticates through an authorization server
# (such as Google or GitHub).
#
# The client receives an authorization code, exchanges it
# for an access token, and then accesses protected APIs.
#
# In this project we use simple JWT authentication.
# The application itself verifies the user's credentials
# and directly issues the JWT without an external
# authorization server.
#
# JWT payloads are Base64 encoded, NOT encrypted.
# Never store passwords or sensitive information inside
# a JWT.
# =====================================================
# GET ALL COURSES (Public)
# =====================================================
@app.get(
    "/api/v1/courses/",
    response_model=schemas.PaginatedCourses
)
def get_courses(
    page: int = Query(1, ge=1),
    page_size: int = Query(2, ge=1),
    search: str = "",
    db: Session = Depends(get_db)
):

    query = db.query(models.Course)

    # Filtering
    if search:
        query = query.filter(
            (models.Course.name.ilike(f"%{search}%")) |
            (models.Course.code.ilike(f"%{search}%"))
        )

    total = query.count()

    offset = (page - 1) * page_size

    courses = query.offset(offset).limit(page_size).all()

    next_page = None
    previous_page = None

    if offset + page_size < total:
        next_page = (
            f"/api/v1/courses/?page={page+1}&page_size={page_size}"
        )

    if page > 1:
        previous_page = (
            f"/api/v1/courses/?page={page-1}&page_size={page_size}"
        )

    return {
        "count": total,
        "next": next_page,
        "previous": previous_page,
        "results": courses
    }


# =====================================================
# GET COURSE BY ID (Public)
# =====================================================
@app.get(
    "/api/v1/courses/{course_id}",
    response_model=schemas.CourseResponse
)
def get_course(
    course_id: int,
    db: Session = Depends(get_db)
):

    course = db.query(models.Course).filter(
        models.Course.id == course_id
    ).first()

    if not course:
        return error_response(
            404,
            "NOT_FOUND",
            f"Course with id {course_id} does not exist"
        )

    return course


# =====================================================
# CREATE COURSE (Protected)
# =====================================================
@app.post(
    "/api/v1/courses/",
    response_model=schemas.CourseResponse,
    status_code=status.HTTP_201_CREATED
)
def create_course(
    course: schemas.CourseCreate,
    response: Response,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    db_course = models.Course(**course.model_dump())

    db.add(db_course)
    db.commit()
    db.refresh(db_course)

    response.headers["Location"] = (
        f"/api/v1/courses/{db_course.id}"
    )

    return db_course


# =====================================================
# UPDATE COURSE (PUT)
# =====================================================
@app.put(
    "/api/v1/courses/{course_id}",
    response_model=schemas.CourseResponse
)
def update_course(
    course_id: int,
    updated_course: schemas.CourseCreate,
    db: Session = Depends(get_db)
):

    course = db.query(models.Course).filter(
        models.Course.id == course_id
    ).first()

    if not course:
        return error_response(
            404,
            "NOT_FOUND",
            f"Course with id {course_id} does not exist"
        )

    course.code = updated_course.code
    course.name = updated_course.name
    course.instructor = updated_course.instructor

    db.commit()
    db.refresh(course)

    return course


# =====================================================
# PARTIAL UPDATE (PATCH)
# =====================================================
@app.patch(
    "/api/v1/courses/{course_id}",
    response_model=schemas.CourseResponse
)
def patch_course(
    course_id: int,
    updated_course: schemas.CourseUpdate,
    db: Session = Depends(get_db)
):

    course = db.query(models.Course).filter(
        models.Course.id == course_id
    ).first()

    if not course:
        return error_response(
            404,
            "NOT_FOUND",
            f"Course with id {course_id} does not exist"
        )

    update_data = updated_course.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(course, key, value)

    db.commit()
    db.refresh(course)

    return course


# =====================================================
# DELETE COURSE (Protected)
# =====================================================
@app.delete(
    "/api/v1/courses/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_course(
    course_id: int,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    course = db.query(models.Course).filter(
        models.Course.id == course_id
    ).first()

    if not course:
        return error_response(
            404,
            "NOT_FOUND",
            f"Course with id {course_id} does not exist"
        )

    db.delete(course)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)