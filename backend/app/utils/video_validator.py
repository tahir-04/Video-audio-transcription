from pathlib import Path
from fastapi import HTTPException, UploadFile

# Allowed video file extensions
ALLOWED_VIDEO_EXTENSIONS = {
    ".mp4",
    ".avi",
    ".mov",
    ".mkv",
    ".wmv",
    ".flv",
    ".webm",
    ".mpeg",
    ".mpg",
    ".m4v",
}

# Allowed MIME types
ALLOWED_VIDEO_MIME_TYPES = {
    "video/mp4",
    "video/x-msvideo",
    "video/quicktime",
    "video/x-matroska",
    "video/x-ms-wmv",
    "video/x-flv",
    "video/webm",
    "video/mpeg",
}

# Maximum upload size (500 MB)
MAX_VIDEO_SIZE = 500 * 1024 * 1024


class VideoValidator:
    @staticmethod
    async def validate(file: UploadFile):
        """
        Validate uploaded video file.
        """

        if file is None:
            raise HTTPException(
                status_code=400,
                detail="No video file uploaded."
            )

        # -----------------------------
        # Validate filename
        # -----------------------------
        if not file.filename:
            raise HTTPException(
                status_code=400,
                detail="Filename cannot be empty."
            )

        extension = Path(file.filename).suffix.lower()

        if extension not in ALLOWED_VIDEO_EXTENSIONS:
            raise HTTPException(
                status_code=400,
                detail=(
                    f"Unsupported video format '{extension}'. "
                    f"Allowed formats: "
                    f"{', '.join(sorted(ALLOWED_VIDEO_EXTENSIONS))}"
                )
            )

        # -----------------------------
        # Validate MIME type
        # -----------------------------
        if file.content_type not in ALLOWED_VIDEO_MIME_TYPES:
            raise HTTPException(
                status_code=400,
                detail=(
                    f"Unsupported content type '{file.content_type}'."
                )
            )

        # -----------------------------
        # Validate file size
        # -----------------------------
        contents = await file.read()

        file_size = len(contents)

        if file_size == 0:
            raise HTTPException(
                status_code=400,
                detail="Uploaded file is empty."
            )

        if file_size > MAX_VIDEO_SIZE:
            raise HTTPException(
                status_code=413,
                detail=(
                    f"Video exceeds maximum size of "
                    f"{MAX_VIDEO_SIZE // (1024 * 1024)} MB."
                )
            )

        # Reset pointer so the file can be saved later
        await file.seek(0)

        return {
            "filename": file.filename,
            "extension": extension,
            "content_type": file.content_type,
            "size": file_size
        }