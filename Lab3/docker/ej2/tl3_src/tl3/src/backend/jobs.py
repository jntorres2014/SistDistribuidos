#!/usr/bin/python3
import os
import cgi
import cgitb
import json
import logging
import sqlalchemy
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

cgitb.enable()

logger= logging.getLogger()
print("Content-Type: application/json;charset=utf-8")
print()

db_string = "postgres://admin:admin@tl3_db:5432/tl3"
engine = create_engine(db_string, echo=False)

metadata = MetaData()

jobs_table = Table('jobs', metadata,
     Column('id', Integer, primary_key=True),
     Column('id_user', String),
     Column('lugar_trabajo', String),
     Column('fecha_inicio', Date),
     Column('fecha_fin', Date),
     Column('cargo', String),
     Column('observacion', String),
)

metadata.create_all(engine) 
Session = sessionmaker(bind=engine)
session = Session()


class Jobs(declarative_base()):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer)
    lugar_trabajo = Column(String)
    fecha_inicio = Column(Date)
    fecha_fin = Column(Date)
    cargo = Column(String)
    observacion = Column(String)

    def __init__(self, id_user, lugar_trabajo, fecha_inicio,
                fecha_fin, cargo, observacion):
        self.id_user = id_user
        self.lugar_trabajo = lugar_trabajo
        self.fecha_fin = fecha_fin
        self.fecha_inicio = fecha_inicio
        self.cargo= cargo
        self.observacion= observacion

def query_jobs():
    logging.exception("HICE LA PETICIOnnnn")
    jobs = []
    logging.exception(session.query(Jobs).all())
    for u in session.query(Jobs).all():
        logging.exception("u")
        job = u.__dict__
        job.pop('_sa_instance_state', None)    
        jobs.append(job)
    logging.exception("VALORES FIN")    
    logging.exception(jobs)
    return jobs

def update_jobs(user):
    #Tomo lo que viene del formulario
    form= cgi.FieldStorage()
    job= Jobs(
        form.getvalue('id_user'),
            form.getvalue('lugar_trabajo'),
            form.getvalue('fecha_inicio'),
            form.getvalue('fecha_fin'),
            form.getvalue('cargo'),
            form.getvalue('observacion')
            )
    session.update(job)
    session.commit()
    

def delete_jobs(id_trabajo):
    job=Jobs.query.get(id_trabajo)
    session.delete(job)
    session.commit()


def create_job():
    try:
        form = cgi.FieldStorage()
        job = Jobs(
            form.getvalue('id_user'),
            form.getvalue('lugar_trabajo'),
            form.getvalue('fecha_inicio'),
            form.getvalue('fecha_fin'),
            form.getvalue('cargo'),
            form.getvalue('observacion')
            )
        session.add(job)
        logging.exception(job)
        session.commit()
        return {'error': False}
    except:
        return {'error': True}


if os.environ['REQUEST_METHOD'] == 'POST':
    logging.exception("Entre al POST")
    response = create_job()
if os.environ['REQUEST_METHOD'] == 'GET':
    response = query_jobs()
    logging.exception("DEVOLVIO")
    logging.exception(response)    
    logging.exception(type(response))
if os.environ['REQUEST_METHOD'] == 'PUT':
   response= update_jobs()
if os.environ['REQUEST_METHOD'] == 'DELETE':
    response = delete_jobs()



print(json.JSONEncoder().encode(response))
