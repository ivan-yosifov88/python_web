from django.urls import path

from exam_2022_02_27.albums_api.views import ListAlbumsView

urlpatterns = (
    path('', ListAlbumsView.as_view()),
)
