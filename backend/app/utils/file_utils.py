import os
import shutil
import uuid
from datetime import datetime
from uuid import uuid4
from pathlib import Path

UPLOAD_DIR = Path("uploads")
OUTPUT_DIR = Path("outputs")

UPLOAD_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

from fastapi import HTTPException, UploadFile

from app.constants import (
    ALLOWED_AUDIO_EXTENSIONS,
    ALLOWED_VIDEO_EXTENSIONS,
    ALLOWED_AUDIO_MIME_TYPES,
    ALLOWED_VIDEO_MIME_TYPES,
    MAX_UPLOAD_SIZE,
)

MAX_FILE_SIZE = 200 * 1024 * 1024

def create_directory(path: str):
    """
    Create directory if it doesn't exist.
    """
    Path(path).mkdir(
        parents=True,
        exist_ok=True
    )

def create_directory(directory: str) -> None:
    """
    Create a directory if it does not already exist.
    """
    Path(directory).mkdir(parents=True, exist_ok=True)

def get_extension(filename: str):
    """
    Return file extension.
    """

    return Path(filename).suffix.lower()

from pathlib import Path

def get_file_extension(filename: str) -> str:
    """
    Return the file extension in lowercase.
    """
    return Path(filename).suffix.lower()


def generate_filename(filename: str):
    """
    Generate unique filename.
    """

    extension = Path(filename).suffix

    unique_name = f"{uuid.uuid4()}{extension}"

    return unique_name

def validate_file_extension(
    filename: str,
    allowed_extensions: list[str]
):
    """
    Validate uploaded file extension.
    Returns 'audio' or 'video'.
    """

    extension = Path(filename).suffix.lower()

    if extension in ALLOWED_AUDIO_EXTENSIONS:
        return "audio"

    if extension in ALLOWED_VIDEO_EXTENSIONS:
        return "video"

    raise HTTPException(
        status_code=400,
        detail=f"Allowed file types: {allowed_extensions}"
    )

def file_exists(filepath: str) -> bool:
    """
    Check whether file exists.
    """

    return Path(filepath).exists()

def validate_content_type(file: UploadFile, file_type: str) -> None:
    """
    Validate uploaded file MIME type.
    """

    if file_type == "audio":
        if file.content_type not in ALLOWED_AUDIO_MIME_TYPES:
            raise HTTPException(
                status_code=400,
                detail="Invalid audio MIME type."
            )

    if file_type == "video":
        if file.content_type not in ALLOWED_VIDEO_MIME_TYPES:
            raise HTTPException(
                status_code=400,
                detail="Invalid video MIME type."
            )
        
def validate_file_size(
    file: UploadFile
):

    file.file.seek(0, 2)

    size = file.file.tell()

    file.file.seek(0)

    if size > MAX_FILE_SIZE:

        raise HTTPException(

            status_code=400,

            detail="File size exceeds 200 MB."

        )
    
def generate_unique_filename(original_filename: str) -> str:
    """
    Generate a unique filename while preserving the extension.
    """
    unique_id = uuid.uuid4().hex

    extension = Path(original_filename).suffix

    unique_name = f"{uuid.uuid4().hex}{extension}"

    #stem = Path(original_filename).stem

    return unique_name

def generate_timestamp_filename(original_filename: str) -> str:
    """
    Generate filename with current timestamp.

    Example:

    meeting.mp3

    →

    20260702_104501_meeting.mp3
    """

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    return f"{timestamp}_{original_filename}"

def delete_file(filepath: str) -> bool:
    """
    Delete a file if it exists.

    Returns True if deleted,
    False otherwise.
    """

    path = Path(filepath)

    if path.exists():
        path.unlink()
        return True

    return False

def save_upload_file(
    file: UploadFile,
    destination: str
) -> None:
    """
    Save uploaded file to disk.
    """

    with open(destination, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

def get_file_size(filepath: str) -> float:
    """
    Return file size in MB.
    """

    path = Path(filepath)

    size = path.stat().st_size

    return round(size / (1024 * 1024), 2)

def copy_file(source: str, destination: str):
    """
    Copy file from source to destination.
    """

    shutil.copy(source, destination)

def move_file(source: str, destination: str):
    """
    Move file from source to destination.
    """

    shutil.move(source, destination)

def get_upload_path(filename: str) -> Path:
    """
    Return full upload path.
    """

    return UPLOAD_DIR / filename

def get_output_path(filename: str) -> Path:
    """
    Return output file path.
    """

    return OUTPUT_DIR / filename

def get_file_metadata(
    file: UploadFile,
    saved_filename: str,
    file_size: int,
    file_type: str,
):
    """
    Return metadata for the uploaded file.
    """

    return {
        "original_filename": file.filename,
        "saved_filename": saved_filename,
        "content_type": file.content_type,
        "size_bytes": file_size,
        "file_type": file_type,
    }

