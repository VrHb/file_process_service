from rest_framework import serializers
from fileprocessapp.models import File


class FileSerializer(serializers.Serializer):
    file = serializers.FileField()

    class Meta:
        fields = ['file']



