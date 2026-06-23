from sqlalchemy import *
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

url = URL.create(
    "mysql+mysqlconnector",
    username="root",
    password="Shamu@2711",
    host="127.0.0.1",
    port=3306,
    database="college_db_orm"
)


engine = create_engine(url, echo=True)

class Department(Base):
    __tablename__ = "departments"

    department_id = Column(Integer, primary_key=True)
    dept_name = Column(String(100), nullable=False)
    head_of_dept = Column(String(100))
    budget = Column(Numeric(12,2))

    students = relationship("Student", back_populates="department")
    professors = relationship("Professor", back_populates="department")
    courses = relationship("Course", back_populates="department")
class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100), unique=True)
    date_of_birth = Column(Date)
    enrollment_year = Column(Integer)
    is_active = Column(Boolean, default=True)

    department_id = Column(
        Integer,
        ForeignKey("departments.department_id")
    )

    department = relationship(
        "Department",
        back_populates="students"
    )

    enrollments = relationship(
        "Enrollment",
        back_populates="student"
    )
    
class Course(Base):
    __tablename__ = "courses"

    course_id = Column(Integer, primary_key=True)
    course_name = Column(String(150))
    course_code = Column(String(20), unique=True)
    credits = Column(Integer)

    department_id = Column(
        Integer,
        ForeignKey("departments.department_id")
    )

    department = relationship(
        "Department",
        back_populates="courses"
    )

    enrollments = relationship(
        "Enrollment",
        back_populates="course"
    )
class Enrollment(Base):
    __tablename__ = "enrollments"

    enrollment_id = Column(Integer, primary_key=True)

    student_id = Column(
        Integer,
        ForeignKey("students.student_id")
    )

    course_id = Column(
        Integer,
        ForeignKey("courses.course_id")
    )

    enrollment_date = Column(Date)
    grade = Column(String(2))

    student = relationship(
        "Student",
        back_populates="enrollments"
    )

    course = relationship(
        "Course",
        back_populates="enrollments"
    )
class Professor(Base):
    __tablename__ = "professors"

    professor_id = Column(Integer, primary_key=True)
    prof_name = Column(String(100))
    email = Column(String(100))
    salary = Column(Numeric(10,2))

    department_id = Column(
        Integer,
        ForeignKey("departments.department_id")
    )

    department = relationship(
        "Department",
        back_populates="professors"
    )
class CourseSchedule(Base):
    __tablename__ = "course_schedules"

    schedule_id = Column(Integer, primary_key=True)

    course_id = Column(
        Integer,
        ForeignKey("courses.course_id")
    )

    day_of_week = Column(String(20))
    start_time = Column(Time)
    end_time = Column(Time)

    course = relationship("Course")
    #Base.metadata.create_all(engine)

#print("Tables created successfully")