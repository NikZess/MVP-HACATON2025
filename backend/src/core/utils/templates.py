from fastapi.templating import Jinja2Templates
from pathlib import Path
import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent.parent.parent.parent
templates = Jinja2Templates(directory=BASE_DIR / "frontend" / "templates")
