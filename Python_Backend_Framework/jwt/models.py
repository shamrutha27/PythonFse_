from sqlalchemy import Column, Integer, String, Boolean
from database import Base


# ----------------------------
# Course Model
# ----------------------------
class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, nullable=False, index=True)
    name = Column(String, nullable=False)
    instructor = Column(String, nullable=False)


# ----------------------------
# User Model
# ----------------------------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    # Email must be unique
    email = Column(String, unique=True, nullable=False, index=True)

    # Never store the user's plain-text password.
    # Store only the bcrypt hash.
    hashed_password = Column(String, nullable=False)

    is_active = Column(Boolean, default=True)