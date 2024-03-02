'''
FastAPI is...
high performance!
faster than Django & Flask!
easy to learn!
fast to code!
ready for production!
'''
# Tip: Asyncio is important for FastAPI!
from fastapi import FastAPI
import typing as tp


app = FastAPI() # create an instance


@app.get("/") # root url
async def root():
    return {"message": "Hello World!"}

@app.post("/hello") # test it in postman
async def post():
    return "Hellooooo!"

