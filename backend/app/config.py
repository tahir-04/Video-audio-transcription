
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict



class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str

    HOST: str
    PORT: int

    DEBUG: bool

    UPLOAD_FOLDER: str = "uploads"
    OUTPUT_FOLDER: str = "outputs"


    MAX_UPLOAD_SIZE: int = 200 * 1024 * 1024

    TEMP_FOLDER: str

    LOG_FOLDER: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


    @property
    def project_root(self) -> Path:
        """
        Returns the backend folder.
        """
        return Path(__file__).resolve().parent.parent

    @property
    def upload_path(self) -> Path:
        """
        Returns the uploads folder path.
        """
        return self.project_root / self.UPLOAD_FOLDER

    @property
    def output_path(self) -> Path:
        """
        Returns the outputs folder path.
        """
        return self.project_root / self.OUTPUT_FOLDER


settings = Settings()