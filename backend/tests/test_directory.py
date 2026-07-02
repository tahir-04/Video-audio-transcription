from app.services.directory_manager import *

create_directories()

print("Upload Exists :", directory_exists(UPLOAD_DIR))
print("Output Exists :", directory_exists(OUTPUT_DIR))

print("Upload Count :", count_files(UPLOAD_DIR))
print("Output Count :", count_files(OUTPUT_DIR))

print("Upload Files :", list_files(UPLOAD_DIR))

print("Upload Size :", get_directory_size(UPLOAD_DIR))

print("Upload Info :", get_directory_info(UPLOAD_DIR))