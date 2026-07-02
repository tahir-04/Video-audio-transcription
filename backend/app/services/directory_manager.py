from pathlib import Path
from app.config import settings

BASE_DIR = Path(__file__).resolve().parent.parent.parent

UPLOAD_DIR = BASE_DIR / settings.UPLOAD_FOLDER
OUTPUT_DIR = BASE_DIR / settings.OUTPUT_FOLDER
TEMP_DIR = BASE_DIR / "temp"
LOG_DIR = BASE_DIR / "logs"


def create_directories():

    directories = [
        UPLOAD_DIR,
        OUTPUT_DIR,
        TEMP_DIR,
        LOG_DIR
    ]

    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)

def directory_exists(directory: Path):

    return directory.exists()

def count_files(directory: Path):

    return len(
        [
            file
            for file in directory.iterdir()
            if file.is_file()
        ]
    )

def list_files(directory: Path):

    files = []

    for file in directory.iterdir():

        if file.is_file():

            files.append(file.name)

    return files

def get_directory_size(directory: Path):

    total = 0

    for file in directory.rglob("*"):

        if file.is_file():

            total += file.stat().st_size

    return total

def delete_file(file_path: Path):

    if file_path.exists():

        file_path.unlink()

        return True

    return False

def clear_directory(directory: Path):

    for file in directory.iterdir():

        if file.is_file():

            file.unlink()

def clean_temp():

    clear_directory(TEMP_DIR)

def get_directory_info(directory: Path):

    return {

        "path": str(directory),

        "exists": directory.exists(),

        "files": count_files(directory),

        "size": get_directory_size(directory)

    }