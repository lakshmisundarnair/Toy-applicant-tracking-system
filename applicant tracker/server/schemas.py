from pydantic import BaseModel

class Baseschema(BaseModel):
    id:int

class Application(BaseModel):
    job_id:int
    user_id:int
    intro:str
    user_name:str
    user_email:str
    qualification:str
    experiance:str
    skills:str
    phone:int

class Jobresponse(BaseModel):
        auther_id:int
        title: str
        company_name: str
        salary: str
        description: str
        job_type: str
        qualification: str
       
   