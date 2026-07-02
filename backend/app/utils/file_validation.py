from pathlib import Path
from fastapi import UploadFile, HTTPException, status

# ---------------------------------------------------------------------
# Allowed Audio Extensions
# ---------------------------------------------------------------------

ALLOWED_AUDIO_EXTENSIONS = {
    ".mp3",
    ".wav",
    ".m4a",
    ".aac",
    ".flac",
    ".ogg",
    ".wma"
}

# ---------------------------------------------------------------------
# Allowed MIME Types
# ---------------------------------------------------------------------

ALLOWED_AUDIO_MIME_TYPES = {
    "audio/mpeg",
    "audio/mp3",
    "audio/wav",
    "audio/x-wav",
    "audio/wave",
    "audio/x-pn-wav",
    "audio/mp4",
    "audio/x-m4a",
    "audio/aac",
    "audio/flac",
    "audio/ogg",
    "audio/x-ms-wma",
    "application/octet-stream",  # Some browsers use this
}

# ---------------------------------------------------------------------
# Maximum File Size
# ---------------------------------------------------------------------

MAX_AUDIO_FILE_SIZE = 100 * 1024 * 1024  # 100 MB


# ---------------------------------------------------------------------
# Validate File Extension
# ---------------------------------------------------------------------

def validate_audio_extension(file: UploadFile) -> None:
    """
    Validate uploaded audio file extension.
    """

    extension = Path(file.filename).suffix.lower()

    if extension not in ALLOWED_AUDIO_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unsupported audio file extension: {extension}"
        )


# ---------------------------------------------------------------------
# Validate MIME Type
# ---------------------------------------------------------------------

def validate_audio_content_type(file: UploadFile) -> None:
    """
    Validate uploaded audio MIME type.
    """

    if file.content_type not in ALLOWED_AUDIO_MIME_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unsupported audio content type: {file.content_type}"
        )


# ---------------------------------------------------------------------
# Validate File Size
# ---------------------------------------------------------------------

async def validate_audio_file_size(file: UploadFile) -> None:
    """
    Validate uploaded audio file size.
    """

    contents = await file.read()

    size = len(contents)

    if size > MAX_AUDIO_FILE_SIZE:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Audio file exceeds maximum allowed size (100 MB)."
        )

    # Reset file pointer so it can be read again later
    await file.seek(0)


# ---------------------------------------------------------------------
# Validate File Name
# ---------------------------------------------------------------------

def validate_audio_filename(file: UploadFile) -> None:
    """
    Ensure uploaded file has a valid filename.
    """

    if not file.filename:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Filename is missing."
        )


# ---------------------------------------------------------------------
# Complete Audio Validation
# ---------------------------------------------------------------------

async def validate_audio_file(file: UploadFile) -> None:
    """
    Perform all audio validations.
    """

    validate_audio_filename(file)

    validate_audio_extension(file)

    validate_audio_content_type(file)

    await validate_audio_file_size(file)