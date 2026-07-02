from typing import Optional

from pydantic import BaseModel, HttpUrl


class URLRequest(BaseModel):

    url: HttpUrl


class URLResponse(BaseModel):

    success: bool

    message: Optional[str] = None

    title: Optional[str] = None

    file_path: Optional[str] = None

    extension: Optional[str] = None

    duration: Optional[int] = None