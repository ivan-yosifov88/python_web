from django.contrib import admin
from django.urls import path, include

urlpatterns = (
    path('admin/', admin.site.urls),
    path('', include('exam_2022_02_27.web_app.url')),
    path('albums_api/', include('exam_2022_02_27.albums_api.url')),
)
