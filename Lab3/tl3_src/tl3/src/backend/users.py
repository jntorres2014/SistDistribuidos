#!/usr/bin/python3
import os
import cgi
import cgitb
import json
import sqlalchemy
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

cgitb.enable()

print("Content-Type: application/json;charset=utf-8")
print()

db_string = "postgres://admin:admin@tl3_db:5432/tl3"
engine = create_engine(db_string, echo=False)

metadata = MetaData()

users_table = Table('users', metadata,
     Column('id', Integer, primary_key=True),
     Column('name', String),
     Column('username', String),
     Column('age', Integer),
     Column('password', String),
)

metadata.create_all(engine) 
Session = sessionmaker(bind=engine)
session = Session()


class User(declarative_base()):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String)
    age = Column(Integer)
    password = Column(String)

    def __init__(self, name, age, username, password):
        self.name = name
        self.age = age
        self.username = username
        self.password = password


def query_users():
    users = []
    for u in session.query(User).all():
        user = u.__dict__
        user.pop('_sa_instance_state', None)    
        users.append(user)
        
    return users

def update_user():
    pass   

def delete_user():
    pass


def create_user():
    try:
        form = cgi.FieldStorage()
        user = User(
            form.getvalue('name'),
            form.getvalue('age'),
            form.getvalue('username'),
            form.getvalue('password')
            )
        session.add(user)
        session.commit()
        return {'error': False}
    except:
        return {'error': True}
    

if os.environ['REQUEST_METHOD'] == 'GET':
    response = query_users()    
if os.environ['REQUEST_METHOD'] == 'POST':
    response = create_user()
#if os.environ['REQUEST_METHOD'] == 'UPDATE'
  #  response = update_user()
#if os.environ['REQUEST_METHOD'] == 'DELETE'
 #   response = delete_user()
if not response:
    response = {}


print(json.JSONEncoder().encode(response))
'''
class Jobs (declarative_base):
    __tablename__ = 'jobs'

    id = Column (Integer, primary_key = True)
    user = Column (Integer, foreing_key=True)
    lugar_trabajo= Column(String)
    fecha_inicio= Column (Date)
    fecha_fin = Column (Date)
    cargo= Column (String)
    observacion= Column (String)
    
    def __init__(self,usuario, lugar_trabajo, fecha_inicio, fecha_fin,cargo,observacion):
        self.usuario = usuario
        self.lugar_trabajo= lugar_trabajo
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.cargo= cargo
        self.observacion= observacion


    def create_cargo():
        try:
            form= cgi.FieldStorage()
            jobs= Jobs(
                form.getvalue('usuario')
                form.getvalue('lugar')
                form.getvalue('f_inicio')
                form.getvalue('f_fin')
                form.getvalue('cargo')
                form.getvalue('observacion'))
            session.add(jobs)
            session.commit()
            return {'error':False}
        except:
            return {'error':True}
'''