'''
It's time to use Path & Query classes for validation params :D
'''
from fastapi import FastAPI, Path, Query
# Path use for validate the Path Parameters! :)
# Query use for validate the Query Parameters! :)
from pydantic import BaseModel


app = FastAPI()

class Person(BaseModel):
    # use Path validator here!
    name: str = Path(
        min_length=2,
        max_length=50,
        title='person name' # makes information clearer
    )
    
    age: int = Path(
        gt=0, # greater than qeual -> 0
        le=100, # little than equal -> 100
        title='person age' # makes information clearer
    )
    
    height: float | None = None

    
# use Query validator here!
@app.post('/person/')
def person(person:Person, father_name:str=Query('idk', min_length=2, max_length=50)): 
    person_info: dict = person.dict()
    person_info.setdefault('father_name', father_name) # add query param to main body
    return person_info

    
# https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/
# https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
# https://docs.pydantic.dev/1.10/usage/schema/#field-customization
