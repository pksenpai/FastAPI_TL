from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel


app = FastAPI()

""" seperate io """
class UserIn(BaseModel): # input data
    username: str
    email: str
    password: str


class UserOut(BaseModel): # output data
    username: str
    email: str
    
    
#___________________________________________________________
"""\______[RESPONSE_MODEL]______/"""
"""
-response_model:
    We shouldn't return sensitive informations
    like passwords, so we have to use response_model.
    this argument specifies what output should be returned :3
"""
@app.post('/profile/', response_model=UserOut)
def user_info(user: UserIn): # receive hole data
    return user # give non-sensitive informations

# https://fastapi.tiangolo.com/tutorial/response-model/#response_model-parameter
#___________________________________________________________

#___________________________________________________________
"""\_______[STATUS_CODE]_______/"""
"""
-Status code:
    An HTTP status code is a server response to a browser's
    request. so it's an important topic in web develpment.
    FastAPI set automatic the status codes but 
    it will be better if we do it ourselves. :3
"""
@app.post('/profile2/', response_model=UserOut, status_code=201) # 201: created successfully
def user_info2(user: UserIn):
    return user

# Tip: If you forget the status codes, try to search, however, FastAPI have a list of status codes ready in status module.
# Tip: FastAPI status is also more human readable
@app.post('/profile3/', response_model=UserOut, status_code=status.HTTP_201_CREATED)
def user_info3(user: UserIn):
    return user

# https://fastapi.tiangolo.com/tutorial/response-status-code/
#___________________________________________________________

#___________________________________________________________
"""\______[ERROR_HANDLING]______/"""
"""
-error handling:
    FastAPI have ready exceptions for show errors but 
    sometimes we need to define exceptions ourselves.
    so use HTTPException for FastAPI.
"""
# Tip: if use the python exceptions in FastAPI, user just receive "500:Internal Server Error"!
@app.post('/profile4/', response_model=UserOut, status_code=201) # 201: created successfully
def user_info4(user: UserIn):
    if user.username.lower() == 'admin':
        raise HTTPException(
            detail="username can't be Admin or admin",
            status_code=status.HTTP_400_BAD_REQUEST
        )
    return user

# https://fastapi.tiangolo.com/tutorial/handling-errors/
#___________________________________________________________
