from app.utils.file_utils import (
    generate_unique_filename,
    generate_timestamp_filename,
    get_file_extension,
    get_upload_path,
    get_output_path,
)

print(generate_unique_filename("lecture.mp4"))
print(generate_timestamp_filename("meeting.mp3"))
print(get_file_extension("movie.MKV"))
print(get_upload_path("video.mp4"))
print(get_output_path("transcript.txt"))