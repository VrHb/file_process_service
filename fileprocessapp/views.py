from datetime import datetime

from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser 


from .serializers import FileSerializer
from .models import File
from .tasks import process_file
from file_process_service.settings import MEDIA_ROOT



class FileUploadView(APIView):
    parser_classes = (MultiPartParser, )
    
    def post(self, request):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            file = File.objects.create(
                file=request.FILES.get('file'),
                uploaded_at=datetime.now(),
                processed=False
            )
            file_path = f'{MEDIA_ROOT}/{file.file}'
            file_processed = process_file.delay(file_path)
            if file_processed:
                file.processed = True
                file.save()
            serialized_file = FileSerializer(file).data
            return JsonResponse(serialized_file, safe=False, status=201)
        return JsonResponse(serializer.errors, status=400)

class FilesView(APIView):

    def get(self, request):
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        serialized_files = serializer.data
        return JsonResponse(serialized_files, safe=False, status=201)

