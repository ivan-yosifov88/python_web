from django.shortcuts import render

from petstagram.main_app.models import Profile, PetPhoto


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def show_home(request):
    context = {
        'hide_additional_nav_items': True
    }
    return render(request, 'home_page.html', context)


def show_dashboard(request):
    profile = get_profile()
    pets = profile.pet_set.all()
    pet_photos = PetPhoto.objects.filter(
        tagged_pets__user_profile=profile
    )
    context = {
        'pet_photos': pet_photos,
    }
    return render(request, 'dashboard.html', context    )


def show_profile(request):
    return render(request, 'profile_details.html')


def show_photo_details(request, pk):
    return render(request, 'photo_details.html')
