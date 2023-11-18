# main.py
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse 
from controllers import login, add_user
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="VACTIC AI ASSESMENT")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/login", response_class=HTMLResponse)
async def login_handler(request: Request, username: str = Form(...), password: str = Form(...)):
    return await login(request, username, password)

@app.post("/add_user", response_class=HTMLResponse)
async def add_user_handler(request: Request, username: str = Form(...), password: str = Form(...)):
    return await add_user(request, username, password)
