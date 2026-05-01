'''
docstring del módulo 
'''

from fastapi import FastAPI, HTTPException

import schemas
import db
from models_db import Student

db.Base.metadata.create_all(db.engine)

# Añade Datos iniciales a la tabla
# lista = [("Ana", 44), ("Ricardo", 37), ("Marina", 32)]
# for x in lista:
#     db.session.add(Student(x[0], x[1]))
# db.session.commit() 


# devuelve la consulta si existe 
def student_check(student_id):
    res = db.session.query(Student).get(student_id)
    if not res:
        raise HTTPException(status_code=404, detail='Student Not Found')
    return res


app = FastAPI()
# KEY = "e7322523fb86ed64c836a979cf8465fbd43637812"


@app.get('/')
def hello():
    return {"greeting":"Hello world"}

@app.get('/status')
def status():
    return {"status":"ok"}

@app.get('/students/', response_model=list[schemas.StudentOut])
def user_list():
    noseusa = 100
    res = db.session.query(Student).all()
    return res

@app.post('/students/', response_model=schemas.StudentOut)
def user_add(alu: schemas.StudentIn):
    new = Student(alu.name, alu.age)
    db.session.add(new)
    db.session.commit()
    return db.session.query(Student).get(new.id)


@app.get('/students/{id}', response_model=schemas.StudentOut)
def user_detail(id: int):
    res = student_check(id)
    return res


@app.delete('/students/{id}', response_model=schemas.StudentOut)
def user_delete(id: int):
    res = student_check(id)
    db.session.delete(res)
    db.session.commit()
    return res


@app.put('/students/{id}', response_model=schemas.StudentOut)
def user_update(id: int, alu: schemas.StudentIn):
    res = student_check(id)
    res.name = alu.name
    res.age = alu.age
    db.session.commit()
    return res
