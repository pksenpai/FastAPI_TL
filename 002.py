'''
HTTP have two parameters:
    1. Path Parameters -> .../123/book_list/
    2. Query Parameters -> .../?page=2&filter=romance
'''
from fastapi import FastAPI
import typing as tp


app = FastAPI()


@app.get("/books/{book_name}") # Path Parameter
async def book_list(book_name: str) -> 'json':
    return {"book": f"{book_name}"}

@app.get("/books/") # Query Parameter
async def book_list(page: int) -> 'json':
    return {"book": f"book list page{page}"}

# Tip: "page: int" & "-> json" is annotations
#      used for show variable dataype
#      in python its just for guiding
#      but in FastAPI it's mandatory!


# https://fastapi.tiangolo.com/tutorial/path-params/
# https://fastapi.tiangolo.com/tutorial/query-params/