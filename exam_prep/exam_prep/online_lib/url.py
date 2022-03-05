from django.urls import path

from exam_prep.online_lib.views import book_details, create_book, create_profile, edit_book, edit_profile, \
    profile_delete, show_index, \
    show_profile

urlpatterns = (
    path('', show_index, name='show index'),
    path('add/', create_book, name='create book'),
    path('edit/<int:pk>/', edit_book, name='edit book'),
    path('details/<int:pk>/', book_details, name='book details'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/', show_profile, name='show profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', profile_delete, name='delete profile'),
)
