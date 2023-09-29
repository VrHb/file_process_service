from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from rest_framework.test import APITestCase

from loguru import logger

from .tasks import process_file


class UploadApiTestCase(APITestCase):
    def test_post(self):
        url = reverse('upload')
        with open('./media/file.txt', 'r') as file:
            logger.info(file)
            response = self.client.post(url, {'file': file})
            logger.info(response)
            self.assertEqual(status.HTTP_201_CREATED, response.status_code)

class FileApiTestCases(APITestCase):
    def test_get(self):
        url = reverse('files')
        response = self.client.get(url)
        logger.info(response)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

class OperationTestCase(TestCase):
    def test_process_file(self):
        result = process_file("./media/file.txt")
        self.assertEqual(True, result)

