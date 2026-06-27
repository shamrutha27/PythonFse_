from typing import Optional

from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import engine, Base, get_db
from models import Course
from schemas import CourseCreate, CourseUpdate, CourseResponse

app = FastAPI(
    title="Course Management API",
    description="FastAPI Course Management System",
    version="1.0",
    contact={
        "name": "Your Name",
        "email": "yourmail@gmail.com"
    }
)


# Create database tables on startup
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# Root Endpoint
@app.get("/")
async def root():
    return {"message": "API running"}


# ---------------------------
# Create Course
# ---------------------------
@app.post(
    "/api/courses/",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Courses"],
    summary="Create a Course",
    response_description="Course Created Successfully"
)
async def create_course(
    course: CourseCreate,
    db: AsyncSession = Depends(get_db)
):
    new_course = Course(**course.model_dump())

    db.add(new_course)
    await db.commit()
    await db.refresh(new_course)

    return new_course


# ---------------------------
# Get Course by ID
# ---------------------------
@app.get(
    "/api/courses/{course_id}",
    response_model=CourseResponse,
    tags=["Courses"]
)
async def get_course(
    course_id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    course = result.scalar_one_or_none()

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return course


# ---------------------------
# Get All Courses
# ---------------------------
@app.get(
    "/api/courses/",
    response_model=list[CourseResponse],
    tags=["Courses"]
)
async def get_courses(
    skip: int = 0,
    limit: int = 10,
    department_id: Optional[int] = None,
    db: AsyncSession = Depends(get_db)
):
    query = select(Course)

    if department_id is not None:
        query = query.where(Course.department_id == department_id)

    query = query.offset(skip).limit(limit)

    result = await db.execute(query)

    return result.scalars().all()


# ---------------------------
# Update Course
# ---------------------------
@app.put(
    "/api/courses/{course_id}",
    response_model=CourseResponse,
    tags=["Courses"]
)
async def update_course(
    course_id: int,
    updated_course: CourseUpdate,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    course = result.scalar_one_or_none()

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    update_data = updated_course.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(course, key, value)

    await db.commit()
    await db.refresh(course)

    return course


# ---------------------------
# Delete Course
# ---------------------------
@app.delete(
    "/api/courses/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Courses"]
)
async def delete_course(
    course_id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    course = result.scalar_one_or_none()

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    await db.delete(course)
    await db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)