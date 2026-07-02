"""
Application-wide constants.

This file stores all upload-related constants so they
are maintained in one place.
"""

# -----------------------------
# Audio File Extensions
# -----------------------------

ALLOWED_AUDIO_EXTENSIONS = {
    ".mp3",
    ".wav",
    ".m4a",
    ".aac",
    ".ogg",
    ".flac"
}

# -----------------------------
# Video File Extensions
# -----------------------------

ALLOWED_VIDEO_EXTENSIONS = {
    ".mp4",
    ".avi",
    ".mov",
    ".mkv",
    ".webm"
}

# -----------------------------
# MIME Types (Audio)
# -----------------------------

ALLOWED_AUDIO_MIME_TYPES = {
    "audio/mpeg",
    "audio/mp3",
    "audio/wav",
    "audio/x-wav",
    "audio/flac",
    "audio/aac",
    "audio/ogg",
    "audio/mp4"
}

# -----------------------------
# MIME Types (Video)
# -----------------------------

ALLOWED_VIDEO_MIME_TYPES = {
    "video/mp4",
    "video/x-msvideo",
    "video/quicktime",
    "video/x-matroska",
    "video/webm"
}

# -----------------------------
# Combined Allowed Types
# -----------------------------

ALLOWED_EXTENSIONS = (
    ALLOWED_AUDIO_EXTENSIONS |
    ALLOWED_VIDEO_EXTENSIONS
)

ALLOWED_MIME_TYPES = (
    ALLOWED_AUDIO_MIME_TYPES |
    ALLOWED_VIDEO_MIME_TYPES
)

MAX_UPLOAD_SIZE = 500 * 1024 * 1024 #500 MB