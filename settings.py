from fastapi.templating import Jinja2Templates


jinja2_templates = Jinja2Templates(directory="templates/")
REDIRECT_URI = "http://127.0.0.1:8000/auth/callback"