from django.utils import timezone

from rest_framework import serializers
from fileprocessapp.models import File


class FileSerializer(serializers.Serializer):
    file = serializers.FileField()
    uploaded_at = serializers.DateTimeField(read_only=True)
    processed = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        file = validated_data.get('file')
        uploaded_at = timezone.now()
        processed = False
        return File.objects.create(
            file=file,
            uploaded_at=uploaded_at,
            processed=processed
        )

    def update(self, instance, validated_data):
        instance.processed = validated_data.get(
            'processed',
            instance.processed
        )
        instance.save()
        return instance



