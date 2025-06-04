import pathlib

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from contextlib import asynccontextmanager

from .core.models import db_helper
from .core.models import Base
from .core.utils.templates import templates

from .api.v1.auth.views import router as auth_router
from .api.v1.users.views import router as users_router
from .api.v1.tasks.views import router as tasks_router
from .api.v1.tasks_daily.views import router as tasks_daily_router
from .api.v1.information.views import router as informations_router
from .api.v1.pages.views import router as pages_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    
app = FastAPI(title="MVP Project", lifespan=lifespan)

app.include_router(router=users_router, prefix="/dashboard/api/v1/users")
app.include_router(router=auth_router, prefix="/api/v1/auth")
app.include_router(router=tasks_router, prefix="/dashboard/api/v1/tasks")
app.include_router(router=tasks_daily_router, prefix="/dashboard/api/v1/tasks")
app.include_router(router=informations_router, prefix="/dashboard/api/v1/info")
app.include_router(router=pages_router)

app.mount("/static", StaticFiles(directory="../frontend/static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("auth.html", {"request": request})

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)