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


def validarUser ():
    #obtengo los usuarios
    form = cgi.FieldStorage()
    logger.exception ("Llegue a validar user")
    logger.exception('Datos del form')
    logger.error(form)
    user=form.getvalue('user')
    password = form.getvalue('pass')
        
    if user1 is None:
        logger.exception ("No existe")
        return {'error': False}
    else:
        #Logguedo
        logger.exception ("Existe Es ")
        logger.debug(user1)
        return {'error': True}         

#Tomamos los valores desde el html 
#form = cgi.FieldStorage()

if os.environ['REQUEST_METHOD'] == 'GET':
    logger.exception ("GET")
    response = validarUser()
if os.environ['REQUEST_METHOD'] == 'POST':
    logger.exception ("POST")
    response = validarUser()  

print(json.JSONEncoder().encode(response))
