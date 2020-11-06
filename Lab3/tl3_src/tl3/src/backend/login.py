#!/usr/bin/python3
import os
import cgi
import cgitb
import json
from backend.users import *
import sqlalchemy
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
cgitb.enable()
metadata.create_all(engine) 
Session = sessionmaker(bind=engine)
session = Session()

def validarUser (nombre, pass):
    user= query_users()
    while     

print("Content-Type: application/json;charset=utf-8")
print()
form = cgi.FieldStorage()
if "name" not in form_input or "pass" not in form_input:
    print("Debe rellenar todos los campos.")
elif validarUser(form.getvalue('name'), form.getvalue('pass'))

