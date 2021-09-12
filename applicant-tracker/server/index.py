from typing import List
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)


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



# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users")#user login
def read_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()


@app.get("/jobs/{user_email}", response_model=List[schemas.Resjob])#job recruiter
def read_user(user_email: str, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_email=user_email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        db_job=crud.get_job(db,id=db_user.id)
        if db_job is None:
            raise HTTPException(status_code=404, detail="Job not found")
        return db_job


@app.get("/applications/{emailid}", response_model=List[schemas.Resapp])#user
def read_application(emailid: str, db: Session = Depends(get_db)):
     db_user = crud.get_user(db, user_email=emailid)
     if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
     else:
        db_app=crud.get_app(db,id=db_user.id)
        if (db_app==[]):
            raise HTTPException(status_code=400, detail="Application not found")
        return db_app

@app.get("/get/jobs/{user_email}")#jobcheckuser
def get_jobs(user_email: str, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_email=user_email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        arr=[]
        query=db.query(models.Job)
        subquery=db.query(models.Application.job_id)
        in_expression=models.Job.id.notin_(subquery.filter(models.Application.user_id==db_user.id))
        db_job=query.filter(in_expression).all()
        for r in db_job:
            arr.append(r) 
        if(arr==[]):
            raise HTTPException(status_code=404, detail="New Jobs not yet created")

    return arr

@app.delete("/application/delete/{delid}")#delete application
def delete_application(delid:int,db: Session = Depends(get_db)):
    db_app=crud.chk_app(db,id=delid)
    if (db_app==[]):
        raise HTTPException(status_code=404, detail="Application not found in that id")
    else:
        delete=db.query(models.Application).filter(models.Application.id==delid).delete()
        db.commit()
    return db.query(models.Application).all()

@app.delete("/job/delete/{delid}")#delete job
def delete_Job(delid:int,db: Session = Depends(get_db)):
    db_app=crud.chk_job(db,id=delid)
    if (db_app==[]):
        raise HTTPException(status_code=404, detail="Job not found in that id")
    else:
        delete=db.query(models.Job).filter(models.Job.id==delid).delete()
        delete_app=db.query(models.Application).filter(models.Application.job_id==delid).delete()
        db.commit()
    return db.query(models.Job).all()

@app.put("/job/edit/{id}")#update job
def update_Job(id:int,job:schemas.Jobresponse,db: Session = Depends(get_db)):
    db_job=crud.chk_job(db,id=id)
    if (db_job==[]):
        raise HTTPException(status_code=404, detail="Job not found in that id")
    else:
        db_edit=crud.update_job(db,job,id=id)
        
    return db_edit
@app.post("/create/job/{mail}")#cretae
def create_job(mail: str,job:schemas.Jobresponse,db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_email=mail)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        db_chk=db.query(models.Job).filter( models.Job.title==job.title,models.Job.author_id==db_user.id,models.Job.company_name==job.company_name).all()
        if(db_chk !=[]):
            raise HTTPException(status_code=404, detail="This Job Already Exist")
        else:
            db_create=crud.create_job(db,job,id=db_user.id)
        return db_create



@app.post("/apply/{email}")#apply job
def create_application(email: str,app:schemas.Applicationres,db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_email=email)
    if (db_user is None):
        raise HTTPException(status_code=404, detail="User not found")
    else:
        db_job=crud.chk_job(db,id=app.job_id)
        if (db_job==[]):
              raise HTTPException(status_code=404, detail="Job not found in that id")
        db_chk=db.query(models.Application).filter( models.Application.job_id==app.job_id,models.Application.user_id==db_user.id).first()
        if(db_chk is None):
            db_app=crud.create_application(db,app,id=db_user.id) 
        else:
            raise HTTPException(status_code=404, detail="Already applied")
    return db_app




