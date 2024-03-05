'''
-ORM:
    Unfortunately, FastAPI does not have its own ORM!
    so we have to use other tools for handle connecting
    between database & FastAPI...
    
    FastAPI recommended SQLAlchemy ORM... :)
'''
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import engine, LocalSession
import schemas, models


models.Base.metadata.create_all(bind=engine)
app = FastAPI()


# def get_db(): # written in doc
#     db = LocalSession()
#     try:
#         yield db
#     finally:
#         db.close()

def get_db(): # my recommended code 
    with LocalSession() as db:
        yield db

@app.post('/user/register/', response_model=schemas.User) # shouldn't return password
def user_create(user_schemas: schemas.CreateUser, db: Session = Depends(get_db)):
    
    email_db = models.User.email
    email_input = user_schemas.email
    print(('x'*30)+'>', email_db)
    print(('x'*30)+'>', email_input)
    
    db_user_email = db.query(models.User).filter(email_db==email_input).first()
    
    if db_user_email:
        # the user object that exists in the database!
        print(('='*30)+'>', db_user_email) # all data from User model is here! :O
        # lets see what's inside the models.User object!
        print(('='*30)+'>', db_user_email.__dict__)
        # lets see what's inside the sqlalchemy obj inside User obj!
        print(('='*30)+'>', db_user_email.__dict__.get('_sa_instance_state').__dict__) 
    
    if db_user_email:
        raise HTTPException(status_code=400, detail="email already exists!")
    
    if 'admin' in user_schemas.username.lower():
        raise HTTPException(
            detail="sorry, username can't contain the word admin or Admin",
            status_code=status.HTTP_400_BAD_REQUEST
        )

    username_db = models.User.username
    username_input = user_schemas.username
    print(('x'*30)+'>', username_db)
    print(('x'*30)+'>', username_input)
    
    db_user_username = db.query(models.User).filter(username_db==username_input).first()
    if db_user_username:
        raise HTTPException(status_code=400, detail="username already exists!")
    
    
    user = models.User(
        email=user_schemas.email,
        username=user_schemas.username,
        password=user_schemas.password
    )
    if not user:
        print("Error: user_create error!")
        raise HTTPException(status_code=400, detail="Sorry, Your account was not created successfully!")
    
    print('='*30, user.__dict__) # new user data
    
    db.add(user) # add in current session
    db.commit() # commit in database
    db.refresh(user)
    return user
    
@app.get('/user/profile/{user_id}', response_model=schemas.User)
def profile(user_id: int, db: Session = Depends(get_db)):
    user_data = db.query(models.User).filter(models.User.id==user_id).first()
    if user_data is None:
        raise HTTPException(status_code=404, detail='user not found!')

    return user_data

    
# https://fastapi.tiangolo.com/tutorial/sql-databases/
# https://www.sqlalchemy.org/

