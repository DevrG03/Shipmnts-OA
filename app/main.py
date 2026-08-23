from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.exception_handlers import register_exception_handlers
from app.api.middleware import RequestLoggingAndTimingMiddleware
from app.api.v1.router import api_v1_router
from app.core.config import get_settings
from app.infrastructure.database.session import engine

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    yield
    # Shutdown - properly dispose database connection pool
    await engine.dispose()


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        version="1.0.0",
        description="RESTful API Backend Application",
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
        lifespan=lifespan,
    )

    # Middlewares
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(RequestLoggingAndTimingMiddleware)

    # Exception Handlers
    register_exception_handlers(app)

    # API Routers
    app.include_router(api_v1_router, prefix=settings.API_V1_STR)

    return app


app = create_app()
