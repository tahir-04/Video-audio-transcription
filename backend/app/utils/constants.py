from pathlib import Path

# Backend root directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent

ALLOWED_AUDIO_EXTENSIONS = {
    ".mp3",
    ".wav",
    ".m4a",
    ".aac",
    ".flac",
    ".ogg",
    ".opus",
    ".wma"
}

# Supported audio formats
SUPPORTED_AUDIO = {
    ".mp3",
    ".wav",
    ".m4a",
    ".aac",
    ".flac",
    ".ogg"
}

# ==========================================================
# Allowed Video File Extensions
# ==========================================================

ALLOWED_VIDEO_EXTENSIONS = {
    ".mp4",
    ".mov",
    ".avi",
    ".mkv",
    ".webm",
    ".flv",
    ".wmv",
    ".mpeg"
}

# Supported video formats
SUPPORTED_VIDEO = {
    ".mp4",
    ".mov",
    ".avi",
    ".mkv",
    ".webm"
}


# ==========================================================
# Allowed Audio MIME Types
# ==========================================================

ALLOWED_AUDIO_MIME_TYPES = {
    "audio/mpeg",
    "audio/mp3",
    "audio/wav",
    "audio/x-wav",
    "audio/flac",
    "audio/x-flac",
    "audio/aac",
    "audio/ogg",
    "audio/opus",
    "audio/x-ms-wma",
    "audio/mp4"
}


# ==========================================================
# Allowed Video MIME Types
# ==========================================================

ALLOWED_VIDEO_MIME_TYPES = {
    "video/mp4",
    "video/x-msvideo",
    "video/x-matroska",
    "video/webm",
    "video/quicktime",
    "video/x-flv",
    "video/x-ms-wmv",
    "video/mpeg"
}


# ==========================================================
# Maximum File Upload Size
# ==========================================================

# 500 MB
MAX_UPLOAD_SIZE = 500 * 1024 * 1024


# ==========================================================
# Upload Directories
# ==========================================================

UPLOAD_DIRECTORY = "uploads"

AUDIO_UPLOAD_DIRECTORY = "uploads/audio"

VIDEO_UPLOAD_DIRECTORY = "uploads/video"

OUTPUT_DIRECTORY = "outputs"

TRANSCRIPT_DIRECTORY = "outputs/transcripts"


# ==========================================================
# Supported URL Platforms
# ==========================================================

SUPPORTED_URL_DOMAINS = {
    "youtube.com",
    "youtu.be",
    "vimeo.com"
}