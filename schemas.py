from pydantic import BaseModel


""" Base User data for inherit """
class BaseUser(BaseModel):
    email: str
    username: str
    
    
""" Input data that should never be returned """
class CreateUser(BaseUser):
    password: str
    
    
""" Response data to user """
class User(BaseUser):
    id: int

    class Config:
        '''
        -What does orm_mode do? (chat-GPT4 anwserd)
            When orm_mode is set to True in the User class,
            the User model is optimized for use in the ORM.
            In other words, when you want to use the User model 
            to create or update records in the database, 
            orm_mode specifies that only fields required 
            for ORM operations (such as reading and writing)
            are extracted from the model, and other fields are ignored.
            This improves performance and reduces overhead, 
            as only necessary data is moved between the application
            and the database.
        '''
        # orm_mode = True
        
        '''
        Tip: this is a warning if using orm_mode name in new version instead of from_attributes:
            .venv/lib/python3.10/site-packages/pydantic/_internal/_config.py:322: UserWarning: Valid config keys have changed in V2:
                * 'orm_mode' has been renamed to 'from_attributes'
                warnings.warn(message, UserWarning)
        '''
        from_attributes = True # use this!

