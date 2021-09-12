from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel



class UserBase(BaseModel):
    id:int
    email: str
    name:str
    type:str

class User(UserBase):
    email:str


    class Config:
        orm_mode = True

class Application(BaseModel):
    id:int
    introduction:str
    qualification:str
    phone:int
    skills:str
    experiance:str
    submitted_on: datetime
    applicant:User

    class Config:
        orm_mode = True

class Job(BaseModel):
    id:int
    title:str
    company_name:str
    salary:str
    job_type:str
    qualification:str
    author_id:int   
    description:str
    created_at:datetime
    class Config:
        orm_mode = True

class Resjob(Job):
    application:List[Application]
    
    class Config:
        orm_mode = True

class Resapp(Application):
    job:Job
    class Config:
        orm_mode = True

class Baseschema(BaseModel):
    author_id:int

class Jobresponse(BaseModel):
        title: str
        company_name: str
        salary: str
        description: str
        job_type: str
        qualification: str

class Applicationres(BaseModel):
    job_id:int
    intro:str
    qualification:str
    experiance:str
    skills:str
    phone:int


