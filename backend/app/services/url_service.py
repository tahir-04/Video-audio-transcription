from app.utils.url_validator import (
    get_url_type
)

from app.services.downloader import MediaDownloader


class URLService:

    @staticmethod
    def download(url: str):

        # Determine URL type
        url_type = get_url_type(url)

        if url_type == "invalid":

            return {
                "success": False,
                "message": "Invalid URL.",
                "url_type": "invalid"
            }

        if url_type == "unsupported":

            return {
                "success": False,
                "message": "Unsupported URL.",
                "url_type": "unsupported"
            }

        downloader = MediaDownloader()
        result = downloader.download(url)

        print(result)

        return result