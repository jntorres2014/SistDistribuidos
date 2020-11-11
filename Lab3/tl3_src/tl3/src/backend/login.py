#!/usr/bin/python3
import os
import cgi
import cgitb
import json
import logging 
import sqlalchemy
from users import User
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

metadata.create_all(engine) 
Session = sessionmaker(bind=engine)
session = Session()



def validarUser ():
    #obtengo los usuarios
    form = cgi.FieldStorage()
    logger.exception ("Llegue a login")
    user1 = session.query(User).all()
    logger.exception (user1)

    logger.exception (form)
    user=form.getvalue('user')
    password = form.getvalue('pass')
    
    if user is None:
        logger.exception ("No existe")
        return False
    else:
        #Logguedo
        logger.exception ("Existe")

        return True         

#Tomamos los valores desde el html 
#form = cgi.FieldStorage()

if os.environ['REQUEST_METHOD'] == 'GET':
    logger.exception ("GET")
    response = validarUser()
if os.environ['REQUEST_METHOD'] == 'POST':
    logger.exception ("POST")
    response = validarUser()  

print(json.JSONEncoder().encode(response))
