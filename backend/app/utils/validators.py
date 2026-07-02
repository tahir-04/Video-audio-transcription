from urllib.parse import urlparse


def is_valid_url(url) -> bool:
    """
    Validate HTTP/HTTPS URLs.
    """

    url = str(url)

    parsed = urlparse(url)

    return (
        parsed.scheme in ("http", "https")
        and bool(parsed.netloc)
    )