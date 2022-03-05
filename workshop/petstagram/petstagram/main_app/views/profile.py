from django.shortcuts import render, redirect

from petstagram.main_app.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from petstagram.main_app.helpers import get_profile
from petstagram.main_app.models import Pet, PetPhoto, Profile


def show_profile(request):
    profile = get_profile()
    pets = Pet.objects.filter(user_profile=profile)
    pet_photos = PetPhoto.objects.filter(tagged_pets__in=pets).distinct()
    # pet_photos = PetPhoto.objects.filter(tagged_pets__user_profile=profile).distinct()

    total_likes_count = sum(pet_p.likes for pet_p in pet_photos)
    total_images_count = len(pet_photos)

    context = {
        'profile': profile,
        'total_likes_count': total_likes_count,
        'total_images_count': total_images_count,
        'pets': pets,
    }
    return render(request, 'profile/profile_details.html', context)


def profile_action(request, form_class, redirect_url, instance, template_name):
    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)
    else:
        form = form_class()
    context = {
        'form': form,
    }
    return render(request, template_name, context)


def create_profile(request):
    return profile_action(
        request, CreateProfileForm, 'index', Profile(), 'profile/profile_create.html')


def edit_profile(request):
    profile = get_profile()
    return profile_action(
        request, EditProfileForm, 'profile details', get_profile(), 'profile/profile_create.html')


def delete_profile(request):

    return profile_action(request, DeleteProfileForm, 'index', get_profile(), 'profile/profile_delete.html')

# def edit_profile(request):
#     profile = get_profile()
#     if request.method == 'POST':
#         form = EditProfileForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile details')
#     else:
#         form = EditProfileForm(instance=profile)
#     context = {
#         'form': form,
#     }
#     return render(request, 'profile/profile_edit.html', context)



