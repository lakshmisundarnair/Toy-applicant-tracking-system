from fastapi import FastAPI
import models
from datetime import datetime
from sqlalchemy.sql import func
from models import user,job,application
from fastapi.middleware.cors import CORSMiddleware
from database import engine,conn
from schemas import Baseschema,Application,Jobresponse

app=FastAPI()
app = FastAPI()
origins= [
    'http://localhost:8000',
    'http://localhost:8080',
    'http://127.0.0.1:8000',
    'http://127.0.0.1:8080'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)



@app.get("/user")
def read_somthing():
    return conn.execute(user.select()).fetchall()
@app.get("/jobs/notapplied/{id}")
def get_jobs(id:int):
    sql="SELECT * FROM jobs j where j.id NOT IN(SELECT job_id FROM applications WHERE user_id=?)"
    q=conn.execute(sql,(id,)).fetchall()
    return q
@app.post("/applied")
def get_applicant(user:Baseschema):
    applications=[]
    query=conn.execute(application.select().where(application.c.user_id==user.id)).fetchall()
    for i in range(len(query)):
        jobs=conn.execute(job.select().where(job.c.id==query[i].job_id)).fetchall()
        arr= {"application":[query[i]],"job":None}
        arr['job']=jobs
        applications.append(arr)
    return applications
@app.post("/application")
def get_application(user:Baseschema):
    applications=[]
    query=conn.execute(job.select().where(job.c.auther_id==user.id)).fetchall()
    for jobs in range(len(query)):
        query2=conn.execute(application.select().where(application.c.job_id==query[jobs].id)).fetchall()
             
        arr= {"job":query[jobs],"applicant":None}
        arr['applicant']=query2
        applications.append(arr)
    return applications
@app.delete("/application/delete")
def delete_application(delid:Baseschema):
    conn.execute(application.delete().where(application.c.id==delid.id))
    return conn.execute(application.select()).fetchall()

@app.post("/application/create")
def create_application(user:Application):
    conn.execute(application.insert().values(
        job_id=user.job_id,
        user_id=user.user_id,
        introduction=user.intro,
        name=user.user_name,
        email=user.user_email,
        qualification=user.qualification,
        experiance=user.experiance,
        skills=user.skills,
        phone=user.phone,
        applied_at=func.now()
    )).fetchall
    return conn.execute(application.select()).fetchall()

@app.delete("/job/delete")
def delete_job(delid:Baseschema):
    conn.execute(job.delete().where(job.c.id==delid.id))
    conn.execute(application.delete().where(application.c.job_id==delid.id))
    return conn.execute(job.select()).fetchall()

@app.get("/jobs/{id}")
def get_job(id:int):
    return conn.execute(job.select().where(job.c.auther_id==id)).fetchall()

@app.post("/create/jobs")
def create_job(jobs:Jobresponse):
    conn.execute(job.insert().values(
        auther_id=jobs.auther_id,
        title=jobs.title,
        company_name=jobs.company_name,
        salary=jobs.salary,
        description=jobs.description,
        job_type=jobs.job_type,
        qualification=jobs.qualification,
        created_at=func.now()
    ))
    return conn.execute(job.select()).fetchall()

@app.put("/edit/jobs/{id}")
def edit_job(id:int,jobs:Jobresponse):
    conn.execute(job.update().values(
        auther_id=jobs.auther_id,
        title=jobs.title,
        company_name=jobs.company_name,
        salary=jobs.salary,
        description=jobs.description,
        job_type=jobs.job_type,
        qualification=jobs.qualification,
        created_at=func.now()
    ).where(job.c.id==id))
    return conn.execute(job.select()).fetchall()
