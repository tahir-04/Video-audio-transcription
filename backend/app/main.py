from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routes.health import router as health_router
from app.routes.upload import router as upload_router
from app.utils.startup import create_directories
from app.routes.url import router as url_router
from app.services.file_manager import file_manager

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_directories()
    yield

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Backend API for VIDEO-AUDIO-TRANSCRIPTION MVP",
)

# ----------------------------------------
# CORS Configuration
# ----------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():

    file_manager.create_directories()

    print("Directories Created Successfully")

@app.get("/", tags=["Home"])
def home():
    return {
        "message": "VIDEO-AUDIO-TRANSCRIPTION API",
        "version": settings.APP_VERSION,
        "status": "Backend Running"
    }

# ----------------------------------------
# Register Routes
# ----------------------------------------
app.include_router(health_router)

app.include_router(upload_router)

app.include_router(url_router)
# ----------------------------------------
# Home Route
# ----------------------------------------

