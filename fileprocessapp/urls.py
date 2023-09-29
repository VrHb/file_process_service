from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from .views import FileUploadView, FilesView 


urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='upload'),
    path('files/', FilesView.as_view(), name='files')

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

