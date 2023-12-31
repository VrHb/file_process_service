import json

from django.http import JsonResponse
from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser 

from loguru import logger


from .serializers import FileSerializer
from .models import File
from .tasks import process_file


class FileUploadView(APIView):
    parser_classes = (MultiPartParser, )

    @logger.catch()
    def post(self, request):
        data = {
            'file': request.FILES.get('file'),
            'uploaded_at': timezone.now(),
            'processed': False
        }
        serializer = FileSerializer(data=data)
        if serializer.is_valid():
            file_object = serializer.save()
            logger.info(file_object)
            file_path = file_object.file.path 
            try:
                file_processed = process_file.delay(file_path)
            except:
                logger.debug(
                    "Redis not run or some problem with celery, file not processed"
                )
                file_processed = False
            if file_processed:
                file_object.processed = True
                file_object.save()
            serialized_file = FileSerializer(file_object).data
            return JsonResponse(serialized_file, safe=False, status=201)
        return JsonResponse(
            serializer.errors,
            status=400,
            json_dumps_params={'ensure_ascii': False}
        )

class FilesView(APIView):

    def get(self, request):
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        serialized_files = serializer.data
        return JsonResponse(serialized_files, safe=False, status=200)

