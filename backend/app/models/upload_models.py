from pydantic import BaseModel, Field
from typing import Optional

class UploadResponse(BaseModel):

    filename: str

    original_filename: str

    content_type: str

    size: int

    path: str

class FileMetadata(BaseModel):

    original_filename: str = Field(
        ...,
        description="Original uploaded filename",
        example="lecture.mp4"
    )

    saved_filename: str = Field(
        ...,
        description="Generated filename stored on the server",
        example="7f4e2b4d-lecture.mp4"
    )

    file_size: int = Field(
        ...,
        description="File size in bytes",
        example=5242880
    )

    content_type: str = Field(
        ...,
        description="Uploaded MIME type",
        example="video/mp4"
    )

    file_extension: str = Field(
        ...,
        description="Uploaded file extension",
        example=".mp4"
    )

    upload_path: str = Field(
        ...,
        description="Location where the file is stored",
        example="uploads/7f4e2b4d-lecture.mp4"
    )

class UploadSuccessResponse(BaseModel):

    success: bool = Field(
        default=True,
        description="Upload status"
    )

    message: str = Field(
        ...,
        description="Success message",
        example="File uploaded successfully."
    )

    data: FileMetadata

class ErrorResponse(BaseModel):

    success: bool = Field(
        default=False,
        description="Operation status"
    )

    error: str = Field(
        ...,
        description="Error message",
        example="Unsupported file type."
    )

    details: Optional[str] = Field(
        default=None,
        description="Additional error information",
        example="Only MP3, WAV, MP4, AVI are supported."
    )

class ValidationErrorResponse(BaseModel):

    success: bool = False

    error: str

    field: str

    value: str