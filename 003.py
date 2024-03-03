'''
-It won't work if your URL character length is
more than 2048 bits! and usually A URL 
should not exceed 2000 characters...

-you shouldn't send sensitive information 
or data with get method in header!

-if you wanna send long or sensitive data
you can use post method in request body...
'''
from fastapi import FastAPI
from typing import Optional, Union # python 3.8 & above
from pydantic import BaseModel


app = FastAPI()

@app.post('/person/')
def person(name: str, age: int, height: float | None = None):
    if height:
        return f"posted {name} with {age} years old & {height}cm height! :3"
    return f"posted {name} with {age} years old! :3"

"""
Tip: If the function parameters are too long,
     you can use the request body (class based) 
     for easier to manage and use!
"""

class Person(BaseModel): # inherited from pydantic.BaseMode
    name: str
    age: int
    height: float | None = None # Python 3.10 & above
    # height: Union[float, None] = None
    # height: Optional[float] = 1

    
@app.post('/person2/')
def person2(person:Person):
    if person.height:
        return \
            f"posted {person.name} with {person.age} years old & {person.height}cm height! :3"
    return \
        f"posted {person.name} with {person.age} years old! :3"
    
    
# https://fastapi.tiangolo.com/tutorial/body/
# https://docs.pydantic.dev/2.6/errors/validation_errors/#missing
