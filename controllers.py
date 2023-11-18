from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models import User

templates = Jinja2Templates(directory="templates")
async def login(request: Request, username: str, password: str):
    user = User.get_user_by_credentials(username, password)
    if user:
        user_list = User.get_all_users()  # Call the static method directly from the class
        return templates.TemplateResponse("add_user.html", {"request": request, "username": username,"user_list": user_list})
    else:
        return templates.TemplateResponse("login.html", {"request": request, "message": "Invalid credentials"})

async def add_user(request: Request, username: str, password: str):
    new_user = User(username, password)
    new_user.save_to_db()
    user_list = User.get_all_users()
    return templates.TemplateResponse("add_user.html", {"request": request, "message": "User added successfully", "username": username,"user_list": user_list})
