from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class VideoUploadResponse(BaseModel):
    success: bool = Field(
        ...,
        description="Indicates whether the upload was successful."
    )

    message: str = Field(
        ...,
        description="Status message."
    )

    file_id: str = Field(
        ...,
        description="Unique identifier for the uploaded file."
    )

    original_filename: str = Field(
        ...,
        description="Original filename provided by the user."
    )

    stored_filename: str = Field(
        ...,
        description="Filename used to store the file on the server."
    )

    file_extension: str = Field(
        ...,
        description="Extension of the uploaded file."
    )

    content_type: str = Field(
        ...,
        description="MIME type of the uploaded file."
    )

    file_size: int = Field(
        ...,
        description="File size in bytes."
    )

    upload_path: str = Field(
        ...,
        description="Location where the file is stored."
    )

    uploaded_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="UTC timestamp when the upload completed."
    )


class ErrorResponse(BaseModel):
    success: bool = False

    message: str

    error_code: Optional[str] = None

    details: Optional[str] = None