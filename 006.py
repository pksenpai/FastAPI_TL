'''
-template:
    Normally, FastAPI is an API creator,
    but you can use the Jinja2 library to
    create a template for personal testing or
    small projects.
-jinja:
    jinja is a fast,
    expressive,
    extensible
    templating engine!
'''
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory='templates') # create object

app.mount("/statics", StaticFiles(directory="statics"), name="static")


@app.get('/', response_class=HTMLResponse) # show response type in doc
def root(request: Request, name: str = "Boss"): # FastAPI need request-obj to loading html-res
    # response our html contains context of request-data & user name
    return \
        templates.TemplateResponse(
            request=request,
            name="home.html",
            context={"name": name.title()}
        )

# https://fastapi.tiangolo.com/advanced/templates/
# https://jinja.palletsprojects.com/en/3.1.x/

