'''
docstring del módulo 
'''

from sqlalchemy import Column, Integer, String
import db


class Student(db.Base):
    '''' docstring '''
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    def __init__(self, nombre, age):
        self.name = nombre
        self.age = age

    # se utiliza al imprimir un student directamente con print
    def __str__(self):
        return " - Nombre: " + self.name + ", Edad: " + str(self.age)

    # se utiliza al imprimir una lista de students directamente con print
    def __repr__(self):
        return f'Student: ({self.name}, {self.age})'

    # Sobre __str_- y __repr__
    #  https://www.analyticslane.com/2020/07/03/diferencias-entre-str-y-repr-en-python/
