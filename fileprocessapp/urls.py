from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

from .views import FileUploadView 


router = routers.DefaultRouter()

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='upload_file_api'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

