import os

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile

from rest_framework import status
from rest_framework.test import APITestCase

from loguru import logger

from .tasks import process_file
from .serializers import FileSerializer
from .models import File


class UploadApiTestCase(APITestCase):
    def test_post(self):
        url = reverse('upload')
        with open('./media/file.txt', 'rb') as file:
            logger.info(file)
            response = self.client.post(url, {'file': file})
            logger.info(response)
            self.assertEqual(status.HTTP_201_CREATED, response.status_code)

class FilesApiTestCases(APITestCase):
    def test_get(self):
        url = reverse('files')
        response = self.client.get(url)
        logger.info(response)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

class OperationTestCase(TestCase):
    def test_process_file(self):
        result = process_file("./media/file.txt")
        self.assertEqual(True, result)

class FileSerializerTestCase(TestCase):
    def test_serializer(self):
        file_object = SimpleUploadedFile('./file0.txt', b'file_content')
        file_object_from_db = File.objects.create(
            file=file_object,
            uploaded_at=timezone.now(),
            processed=False
        )
        serialized_file = FileSerializer(file_object_from_db).data
        required_data = {
            'file': '/media/file0.txt', 
            'uploaded_at': file_object_from_db.uploaded_at.isoformat(),
            'processed': False
        }
        os.remove(file_object_from_db.file.path)
        logger.info(serialized_file)
        logger.info(required_data)
        self.assertEqual(serialized_file, required_data)

    
