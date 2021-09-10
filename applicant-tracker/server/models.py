from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,DateTime,Table
from sqlalchemy.sql import func
from database import engine
from sqlalchemy import MetaData
from typing import List
metadata=MetaData()
user =Table( "users",metadata,

    Column("id",Integer, primary_key=True, autoincrement="auto"),
    Column("email",String, unique=True),
    Column("name",String,nullable=False),
    Column("password",String,nullable=False),
    Column("type",String,nullable=False))

job=Table("jobs",metadata,

    Column("id",Integer, primary_key=True, index=True),
    Column("auther_id",Integer,ForeignKey("users.id"), index=True),
    Column("title",String,nullable=False),
    Column("company_name",String,nullable=False),
    Column("description",String),
    Column("job_type",String),
    Column("salary",String,nullable=False),
    Column("qualification",String),
    Column("created_at",DateTime,server_default=func.now()),
   )

application = Table("applications",metadata,

    Column("id",Integer, primary_key=True, index=True),
    Column("job_id",Integer,ForeignKey("jobs.id"),nullable=False),
    Column("user_id",Integer,ForeignKey("users.id"),nullable=False),
    Column("introduction",String),
    Column("email",String, unique=True),
    Column("name",String,nullable=False),
    Column("phone",Integer,nullable=False),
    Column("skills",String),
    Column("experiance",String,nullable=False),
    Column("qualification",String),
    Column("applied_at",DateTime,server_default=func.now()),    
    )
metadata.create_all(engine)



