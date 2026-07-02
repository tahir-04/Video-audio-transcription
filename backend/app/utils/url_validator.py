from urllib.parse import urlparse
import re

SUPPORTED_DOMAINS = {

    "youtube.com",
    "www.youtube.com",

    "youtu.be",

    "music.youtube.com",

    "m.youtube.com"

}

SUPPORTED_AUDIO = {

    ".mp3",

    ".wav",

    ".m4a",

    ".aac",

    ".ogg",

    ".flac"

}

SUPPORTED_VIDEO = {

    ".mp4",

    ".mov",

    ".avi",

    ".mkv",

    ".webm",

    ".flv"

}

def is_valid_url(url: str) -> bool:

    regex = re.compile(

        r"^(http|https)://"

        r"(([A-Za-z0-9-]+\.)+[A-Za-z]{2,})"

        r"(:\d+)?"

        r"(/.*)?$"

    )

    return re.match(regex, url) is not None

def is_youtube_url(url: str) -> bool:

    parsed = urlparse(url)

    domain = parsed.netloc.lower()

    return domain in SUPPORTED_DOMAINS

def is_audio_url(url: str) -> bool:

    lower = url.lower()

    for extension in SUPPORTED_AUDIO:

        if lower.endswith(extension):

            return True

    return False

def is_video_url(url: str) -> bool:

    lower = url.lower()

    for extension in SUPPORTED_VIDEO:

        if lower.endswith(extension):

            return True

    return False

def get_url_type(url: str):

    if not is_valid_url(url):

        return "invalid"

    if is_youtube_url(url):

        return "youtube"

    if is_audio_url(url):

        return "audio"

    if is_video_url(url):

        return "video"

    return "unsupported"