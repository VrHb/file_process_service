from rest_framework import serializers
from fileprocessapp.models import File


class FileSerializer(serializers.Serializer):
    file = serializers.FileField()
    uploaded_at = serializers.DateTimeField(read_only=True)
    processed = serializers.BooleanField(read_only=True)

    class Meta:
        fields = ['__all__']



