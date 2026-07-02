import browser_cookie3
from pathlib import Path
import yt_dlp 

from app.logger import logger


class MediaDownloader:
    """
    Downloads media from a given URL using yt-dlp.
    """

    def __init__(self):

        self.download_folder = Path("uploads")

        self.download_folder.mkdir(
            parents=True,
            exist_ok=True
        )

    @staticmethod
    def download(url: str):

        try:

            ydl_opts = {
                "outtmpl": str(
                    MediaDownloader().download_folder / "%(title)s.%(ext)s"
                ),

                "format": "bestvideo+bestaudio/best",

                "quiet": False,

                "noplaylist": True,

                "restrictfilenames": True,

                "http_headers": {
                    "User-Agent": (
                        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                        "AppleWebKit/537.36 "
                        "(KHTML, like Gecko) "
                        "Chrome/137.0.0.0 Safari/537.36"
                    )
                },

                #"cookiesfrombrowser": ("chrome",),
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:

                info = ydl.extract_info(
                    url,
                    download=True
                )

                file_path = Path(
                    ydl.prepare_filename(info)
                )

                logger.info(
                    f"Downloaded: {file_path.name}"
                )

                return {

                    "success": True,

                    "title": info.get("title"),

                    "file_path": str(file_path),

                    "extension": file_path.suffix,

                    "duration": info.get("duration")

                }

        except Exception as e:

            logger.error(e)

            return {

                "success": False,

                "message": str(e)

            }

    @staticmethod    
    def download_media(url: str):
        downloader = MediaDownloader()
        return downloader.download(url)