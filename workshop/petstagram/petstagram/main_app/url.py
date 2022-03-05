from django.urls import path

from petstagram.main_app.views.common import show_home, show_dashboard
from petstagram.main_app.views.pet import create_pet, edit_pet, delete_pet
from petstagram.main_app.views.pet_photo import like_pet_photo, show_pet_photo_details, add_pet_photo, edit_pet_photo
from petstagram.main_app.views.profile import show_profile, create_profile, edit_profile, delete_profile

urlpatterns = (
    path('', show_home, name='index'),
    path('dashboard/', show_dashboard, name='dashboard'),

    path('photo/details/<int:pk>/', show_pet_photo_details, name='pet photo details'),
    path('photo/like/<int:pk>/', like_pet_photo, name='like pet photo'),
    path('photo/add/', add_pet_photo, name='add pet photo'),
    path('photo/edit/<int:photo_id>/', edit_pet_photo, name='edit pet photo'),

    path('pet/add/', create_pet, name='add pet'),
    path('pet/edit/<int:pk>/', edit_pet, name='edit pet'),
    path('pet/like/<int:pk>/', delete_pet, name='delete pet'),

    path('profile/', show_profile, name='profile details'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
)
