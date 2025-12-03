import os

def read_file(file_path):
    working_directory = "./"

    wd_abs = os.path.abspath(working_directory)
    target_abs = os.path.abspath(os.path.join(working_directory, file_path))

    # boundary check first
    if not (target_abs == wd_abs or target_abs.startswith(wd_abs + os.sep)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    # must be a file
    if not os.path.isfile(target_abs):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(target_abs, "r") as f:
            file_content_string = f.read()
            return file_content_string
    except Exception as e:
        return f"Error: {e}"