from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,DateTime
from sqlalchemy.orm import relationship
from database import Base

class User(Base):

    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name=Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    type = Column(String)
    jobs=relationship("Job",back_populates="owner")
    application=relationship("Application",back_populates="applicant")


class Job(Base):

    __tablename__ = "jobs"


    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    company_name = Column(String, index=True)
    salary = Column(String, index=True)
    job_type = Column(String, index=True)
    qualification = Column(String, index=True)
    author_id = Column(Integer, ForeignKey("users.id"))
    created_at=Column(DateTime)
    application=relationship("Application",back_populates="job")
    owner = relationship("User",back_populates="jobs")

class Application(Base):

    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer,ForeignKey("jobs.id"))
    user_id = Column(Integer,ForeignKey("users.id"))
    introduction = Column(String, index=True)
    qualification = Column(String, index=True)
    skills = Column(String)
    experiance = Column(String)
    phone = Column(Integer)
    submitted_on=Column(DateTime)
    applicant= relationship("User",back_populates="application")
    job=relationship("Job",back_populates="application")
