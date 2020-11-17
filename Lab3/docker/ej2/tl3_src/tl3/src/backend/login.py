#!/usr/bin/python3
import os
import cgi
import cgitb
import json
import sqlalchemy
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging

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
    user=form.getvalue('user')
    passw = form.getvalue('pass')
    logger.exception("VALORES QUE ENTRAN")
    logger.exception(user)
    logger.exception(passw)
    logger.exception(session.query(User).all())
    for u in session.query(User).all():
        logger.exception("VALORES QUE EXISTEN")
        logger.exception(u.username)
        logger.exception(u.password)
        logger.exception(u.username == user)
        logger.exception(u.password == passw)
        if (u.username == user) and (u.password == passw):
            logger.exception ("EXISTEEEE ")
            return {'error': True}
    return {'error': False}
    

if os.environ['REQUEST_METHOD'] == 'GET':
    logger.exception ("GET")
    response = validarUser()
if os.environ['REQUEST_METHOD'] == 'POST':
    logger.exception ("POST")
    response = validarUser()  

print(json.JSONEncoder().encode(response))
