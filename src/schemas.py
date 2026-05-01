'''
docstring del módulo 
'''

from pydantic import BaseModel, ConfigDict


class StudentIn(BaseModel):
    '''' docstring '''
    name: str
    age: int

    # class Config:
    #     orm_mode = True


class StudentOut(BaseModel):
    '''' docstring '''
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    age: int

    # class Config:
    #     # orm_mode = True
    #     from_attributes = True
