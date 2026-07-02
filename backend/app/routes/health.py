from fastapi import APIRouter

router = APIRouter()


@router.get(
    "/health",
    tags=["Health"]
)
def health_check():

    return {
        "status": "success",
        "message": "Backend is running",
        "service": "VIDEO-AUDIO-TRANSCRIPTION API"
    }