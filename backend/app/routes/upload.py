from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import HTTPException
from app.services.file_manager import FileManager
from app.services.upload_service import UploadService
from app.constants import (
    ALLOWED_AUDIO_EXTENSIONS,
    ALLOWED_VIDEO_EXTENSIONS,
)

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)

upload_service = UploadService()
file_manager = FileManager()

@router.post("/audio")
async def upload_audio(
    file: UploadFile = File(...)
):

    try:

        result = upload_service.save_file(
            file=file,
            allowed_extensions=ALLOWED_AUDIO_EXTENSIONS
        )

        return {
            "success": True,
            "message": "Audio uploaded successfully.",
            "data": result
        }

    except HTTPException as e:
        raise e

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.post("/video")
async def upload_video(
    file: UploadFile = File(...)
):

    try:

        result = upload_service.save_file(
            file=file,
            allowed_extensions=ALLOWED_VIDEO_EXTENSIONS
        )

        return {
            "success": True,
            "message": "Video uploaded successfully.",
            "data": result
        }

    except HTTPException as e:
        raise e

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    
@router.post("/media")
async def upload_media(file: UploadFile = File(...)):

    file_manager.create_upload_directory()

    filename = file_manager.generate_unique_filename(file.filename)

    saved_path = await file_manager.save_uploaded_file(
        upload_file=file,
        filename=filename
    )

    metadata = file_manager.get_file_metadata(saved_path)

    return {
        "message": "Upload successful",
        "file": metadata
    }