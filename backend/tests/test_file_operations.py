from pathlib import Path

from app.utils.file_operations import FileOperations

# Create uploads directory
FileOperations.create_directory("uploads")

# Generate unique filename
filename = FileOperations.generate_unique_filename("meeting.mp4")

print("=" * 50)
print("Generated Filename")
print("=" * 50)
print(filename)

print("\nExtension:")
print(FileOperations.get_extension(filename))

print("\nFilename:")
print(FileOperations.get_filename(filename))

# Create a sample file
sample_file = Path("uploads/sample.txt")
sample_file.write_text("Hello from FileOperations!")

print("\nFile Exists:")
print(FileOperations.exists(str(sample_file)))

print("\nFile Size:")
size = FileOperations.get_file_size(str(sample_file))
print(size, "bytes")

print("\nReadable Size:")
print(FileOperations.human_readable_size(size))

print("\nFile Info:")
print(FileOperations.get_file_info(str(sample_file)))

print("\nDelete File:")
print(FileOperations.delete_file(str(sample_file)))

print("\nExists After Delete:")
print(FileOperations.exists(str(sample_file)))