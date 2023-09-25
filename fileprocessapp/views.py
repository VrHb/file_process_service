from datetime import datetime

from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser 

from .serializers import FileSerializer
from .models import File



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
            return JsonResponse("file uploaded!", safe=False, status=201)
        return JsonResponse(serializer.errors, status=400)
