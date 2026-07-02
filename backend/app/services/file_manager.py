from pathlib import Path

from app.config import settings


class FileManager:

    def __init__(self):

        self.upload_dir = Path(settings.UPLOAD_FOLDER)

        self.output_dir = Path(settings.OUTPUT_FOLDER)

        self.temp_dir = Path(settings.TEMP_FOLDER)

        self.log_dir = Path(settings.LOG_FOLDER)

    def create_directories(self):

        self.upload_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        self.temp_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        self.log_dir.mkdir(
            parents=True,
            exist_ok=True
        )

    def get_upload_directory(self):

        return self.upload_dir

    def get_output_directory(self):

        return self.output_dir

    def get_temp_directory(self):

        return self.temp_dir

    def get_log_directory(self):

        return self.log_dir


file_manager = FileManager()