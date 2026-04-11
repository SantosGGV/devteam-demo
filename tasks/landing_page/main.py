from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

try:
    app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
except Exception:
    pass

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
