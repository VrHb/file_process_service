import os
from file_process_service.celery import app


class FileNotExistsException(Exception):
    pass


@app.task
def process_file(file_path):
    file_check = os.path.exists(file_path)
    if file_check:
        with open(file_path, 'a+') as file:
            file.write('Add line to file!')
        return True
    raise FileNotExistsException("File not exists!") 
