from fastapi import APIRouter

from app.models.url_model import (
    URLRequest,
    URLResponse
)

from app.services.url_service import URLService
from app.services.file_manager import FileManager

router = APIRouter(
    prefix="/url",
    tags=["URL Download"]
)

file_manager = FileManager()

@router.post(
    "/download",
    response_model=URLResponse
)
def download_media(request: URLRequest):

    result = URLService.download(
        str(request.url)
    )

    return result