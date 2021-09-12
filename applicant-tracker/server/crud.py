from sqlalchemy.orm import Session
import models, schemas
from sqlalchemy.sql import func
def get_user(db: Session, user_email: str):

    return db.query(models.User).filter(models.User.email == user_email).first()

def get_job(db: Session, id: int):

    return db.query(models.Job).filter(models.Job.author_id == id).all()
def chk_job(db: Session, id: int):

    return db.query(models.Job).filter(models.Job.id == id).all()
    
def get_app(db: Session, id: int):

    return db.query(models.Application).filter(models.Application.user_id == id).all()
def chk_app(db: Session, id: int):

    return db.query(models.Application).filter(models.Application.id == id).all()



def update_job(db: Session,jobs:schemas.Jobresponse,id:int):
    db_job =db.query(models.Job).filter(models.Job.id==id).first()
    db_job.title=jobs.title
    db_job.company_name=jobs.company_name
    db_job.salary=jobs.salary
    db_job.description=jobs.description
    db_job.job_type=jobs.job_type
    db_job.qualification=jobs.qualification
    db_job.created_at=func.now()
    db.commit()
    db.refresh(db_job)
    return db_job

def create_job(db: Session,jobs:schemas.Jobresponse,id:int):
    db_job = models.Job(author_id=id,
        title=jobs.title,
        company_name=jobs.company_name,
        salary=jobs.salary,
        description=jobs.description,
        job_type=jobs.job_type,
        qualification=jobs.qualification,
        created_at=func.now())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job






def create_application(db: Session,user:schemas.Applicationres,id: int):#create application
    db_get=id
    db_app =models.Application(job_id=user.job_id,user_id=id,introduction=user.intro,qualification=user.qualification,experiance=user.experiance,skills=user.skills,phone=user.phone,submitted_on=func.now())
    db.add(db_app)
    db.commit()
    db.refresh(db_app)
    return db_app
