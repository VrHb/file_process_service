from file_process_service.celery import app

@app.task
def process_file(file_path):
    with open(file_path, 'a+') as file:
        file.write('Add line to file!')
    return True
