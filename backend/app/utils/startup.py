from app.config import settings


def create_directories() -> None:
    """
    Create required application directories.
    """

    settings.upload_path.mkdir(
        parents=True,
        exist_ok=True
    )

    settings.output_path.mkdir(
        parents=True,
        exist_ok=True
    )