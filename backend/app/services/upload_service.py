from pathlib import Path
import shutil
import uuid
from fastapi import UploadFile, HTTPException

from app.utils.video_validator import VideoValidator

from app.utils.file_utils import (
    generate_unique_filename,
    validate_file_extension,
    validate_file_size
)

from app.config import settings

# Upload directory
UPLOAD_DIR = Path("uploads/audio")

# Create directory if it doesn't exist
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


class AudioUploadService:

    @staticmethod
    async def save_audio(file: UploadFile):

        try:
            # Generate unique filename
            unique_filename = (
                f"{uuid.uuid4().hex}_{file.filename}"
            )

            file_path = UPLOAD_DIR / unique_filename

            # Save file
            with file_path.open("wb") as buffer:
                shutil.copyfileobj(file.file, buffer)

            # Get file size
            file_size = file_path.stat().st_size

            return {
                "filename": unique_filename,
                "original_filename": file.filename,
                "content_type": file.content_type,
                "size": file_size,
                "path": str(file_path)
            }

        except Exception as e:

            raise HTTPException(
                status_code=500,
                detail=f"Failed to save file : {str(e)}"
            )
        
async def save_video(file: UploadFile):
        video_info = await VideoValidator.validate(file)
        return {
            "filename": file.filename,
            "content_type": file.content_type
        }

class UploadService:
    """
    Handles common upload operations for
    audio and video files.
    """

    def __init__(self):

        self.upload_dir = Path(settings.UPLOAD_FOLDER)

        self.upload_dir.mkdir(
            parents=True,
            exist_ok=True
        )

    def save_file(
        self,
        file: UploadFile,
        allowed_extensions: list[str]
    ) -> dict:
        """
        Validate and save uploaded file.

        Returns metadata.
        """

        validate_file_extension(
            file.filename,
            allowed_extensions
        )

        validate_file_size(file)

        filename = generate_unique_filename(
            file.filename
        )

        destination = self.upload_dir / filename

        with destination.open("wb") as buffer:
            shutil.copyfileobj(
                file.file,
                buffer
            )

        size = destination.stat().st_size

        return {

            "filename": filename,

            "original_filename": file.filename,

            "content_type": file.content_type,

            "size": size,

            "path": str(destination)

        }
