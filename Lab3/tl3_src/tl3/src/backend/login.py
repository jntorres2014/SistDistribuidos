import os
import cgi
import cgitb
import json
import logging 
from backend.users import *
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

metadata.create_all(engine) 
Session = sessionmaker(bind=engine)
session = Session()



def validarUser ():
    #obtengo los usuarios
    user=form.getvalue('user')
    password = form.getvalue('pass')
    user = session.query(User).filter(User.name == user).filter(User.password == password)
    if user is None:
        logger.exception ("Llegue a login")
        return False
    else:
        #Logguedo
        return True         


logger.exception ("Llegue a login")
logger.exception ("Llegue a login")
logger.exception ("Llegue a login")
#Tomamos los valores desde el html 
form = cgi.FieldStorage()

if os.environ['REQUEST_METHOD'] == 'GET':
    import pdb; pdb.set_trace()
    logger.exception ("Llegue a login")
    logger.exception ("Llegue a login")
    logger.exception ("Llegue a login")
    import pdb; pdb.set_trace()
    response = validarUser()
if os.environ['REQUEST_METHOD'] == 'POST':

    logger.exception ("Llegue a login")
    logger.exception ("Llegue a login")
    logger.exception ("Llegue a login")
    import pdb; pdb.set_trace()
    response = validarUser()  


print({'a':'asd'})
