from pathlib import Path
import shutil
import uuid
from fastapi import UploadFile, HTTPException

# Upload directory
UPLOAD_DIR = Path("uploads/videos")

# Create directory if it doesn't exist
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


class VideoUploadService:

    @staticmethod
    async def save_video(file: UploadFile):

        try:
            # Generate unique filename
            unique_filename = (
                f"{uuid.uuid4().hex}_{file.filename}"
            )

            # Full file path
            file_path = UPLOAD_DIR / unique_filename

            # Save uploaded file
            with file_path.open("wb") as buffer:
                shutil.copyfileobj(file.file, buffer)

            return {
                "status": "success",
                "message": "Video uploaded successfully.",
                "filename": unique_filename,
                "original_filename": file.filename,
                "content_type": file.content_type,
                "file_path": str(file_path),
                "file_size": file_path.stat().st_size
            }

        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Unable to save video: {str(e)}"
            )

        finally:
            file.file.close()