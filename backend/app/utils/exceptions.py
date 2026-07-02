from fastapi import HTTPException, status


class FileValidationException(HTTPException):
    """Base exception for file validation errors."""

    def __init__(self, detail: str):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail,
        )


class InvalidFileExtensionException(FileValidationException):
    """Raised when the uploaded file extension is not allowed."""

    def __init__(self, extension: str, allowed_extensions: list[str]):
        super().__init__(
            detail=(
                f"Invalid file extension '{extension}'. "
                f"Allowed extensions: {', '.join(allowed_extensions)}"
            )
        )


class InvalidMimeTypeException(FileValidationException):
    """Raised when the uploaded file MIME type is not allowed."""

    def __init__(self, mime_type: str, allowed_mime_types: list[str]):
        super().__init__(
            detail=(
                f"Invalid MIME type '{mime_type}'. "
                f"Allowed MIME types: {', '.join(allowed_mime_types)}"
            )
        )


class FileTooLargeException(FileValidationException):
    """Raised when the uploaded file exceeds the maximum allowed size."""

    def __init__(self, file_size: int, max_size: int):
        super().__init__(
            detail=(
                f"File size ({file_size} bytes) exceeds the maximum "
                f"allowed size of {max_size} bytes."
            )
        )


class EmptyFileException(FileValidationException):
    """Raised when the uploaded file is empty."""

    def __init__(self):
        super().__init__(
            detail="Uploaded file is empty."
        )


class MissingFilenameException(FileValidationException):
    """Raised when the uploaded file has no filename."""

    def __init__(self):
        super().__init__(
            detail="Filename is missing."
        )


class FileSaveException(HTTPException):
    """Raised when saving the uploaded file fails."""

    def __init__(self):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to save uploaded file."
        )


class UploadDirectoryException(HTTPException):
    """Raised when the upload directory cannot be created or accessed."""

    def __init__(self):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Upload directory is unavailable."
        )