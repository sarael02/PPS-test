'''
docstring del módulo 
'''

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ruta relativa y nombre de la BD
engine = create_engine('sqlite:///students.db')

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()  # se usará en el modelo de la BD
