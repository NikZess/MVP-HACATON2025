from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from ...core.utils.templates import templates

router = APIRouter()

@router.get("/dashboard", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
