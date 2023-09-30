import os
from file_process_service.celery import app


class FileNotExistsException(Exception):
    pass


@app.task
def process_file(file_path):
    file_exists = os.path.exists(file_path)
    if not file_exists:
        raise FileNotExistsException("File not exists!") 
    with open(file_path, 'a+') as file:
        file.write('Add line to file!')
    return True
