from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from .routes import auth, api_key, credits
from .database import engine
from . import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

app.mount("/static", StaticFiles(directory="app/templates"), name="static")

app.include_router(auth.router, prefix="/auth")
app.include_router(api_key.router, prefix="/api")
app.include_router(credits.router, prefix="/credits")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/use_credits", response_class=HTMLResponse)
def use_credits_page(request: Request):
    return templates.TemplateResponse("use_credits.html", {"request": request})
