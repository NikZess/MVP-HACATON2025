from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from contextlib import asynccontextmanager

from .core.models import db_helper
from .core.models import Base

from .api.tasks.views import router as tasks_router
from .api.auth.views import router as auth_router
from .api.users.views import router as users_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    
app = FastAPI(title="MVP Project", lifespan=lifespan)

app.include_router(router=users_router, prefix="/api/v1/users")
app.include_router(router=auth_router, prefix="/api/v1/auth")
app.include_router(router=tasks_router, prefix="/api/v1/tasks")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)