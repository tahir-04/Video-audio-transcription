import os
import shutil
import uuid
from pathlib import Path

class FileOperations:
    """
    Utility class for handling
    all file-related operations.
    """
    @staticmethod
    def generate_unique_filename(filename: str):

        extension = Path(filename).suffix

        unique_name = f"{uuid.uuid4()}{extension}"

        return unique_name
    
    @staticmethod
    def get_extension(filename: str):

        return Path(filename).suffix.lower()
    
    @staticmethod
    def get_filename(filename: str):

        return Path(filename).stem
    
    @staticmethod
    def exists(path: str):

        return os.path.exists(path)
    
    @staticmethod
    def create_directory(path: str):

        os.makedirs(path, exist_ok=True)

    @staticmethod
    def delete_file(path: str):

        if os.path.exists(path):

            os.remove(path)

            return True

        return False
    
    @staticmethod
    def copy_file(source, destination):

        shutil.copy2(source, destination)

    @staticmethod
    def move_file(source, destination):

        shutil.move(source, destination)

    @staticmethod
    def get_file_size(path: str):

        if os.path.exists(path):

            return os.path.getsize(path)

        return 0
    
    @staticmethod
    def human_readable_size(size):

        units = [
            "B",
            "KB",
            "MB",
            "GB"
        ]

        for unit in units:

            if size < 1024:

                return f"{size:.2f} {unit}"

            size /= 1024

        return f"{size:.2f} TB"
    
    @staticmethod
    def get_file_info(path: str):

        if not os.path.exists(path):

            return None

        return {

            "filename": Path(path).name,

            "extension": Path(path).suffix,

            "size": FileOperations.get_file_size(path),

            "readable_size": FileOperations.human_readable_size(
                FileOperations.get_file_size(path)
            ),

            "absolute_path": os.path.abspath(path)

        }