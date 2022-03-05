from django.shortcuts import render, redirect

from exam_2022_02_27.web_app.forms import CreateProfileForm, CreateAlbumForm, EditAlbumForm, DeleteAlbumForm, \
    DeleteProfileForm
from exam_2022_02_27.web_app.models import Profile, Album


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def get_album():
    albums = Album.objects.all()
    if albums:
        return albums
    return None


def profile_action(request, form_class, instance, redirect_url, template_view):
    if request.method == "POST":
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)
    else:
        form = form_class(instance=instance)
    context = {
        'form': form,
    }
    return render(request, template_view, context)


def album_action(request, form_class, instance, redirect_url, template_view):
    if request.method == "POST":
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)
    else:
        form = form_class(instance=instance)
    context = {
        'form': form,
        'album': instance,
    }
    return render(request, template_view, context)


def show_home(request):
    profile = get_profile()
    albums = get_album()
    if not profile:
        return redirect('create profile')
    context = {
        'albums': albums
    }
    return render(request, 'home-with-profile.html', context)


def create_profile(request):
    return profile_action(request, CreateProfileForm, Profile(), 'show profile details', 'home-no-profile.html')


def delete_profile(request):
    return profile_action(request, DeleteProfileForm, get_profile(), 'show index', 'profile-delete.html')


def profile_details(request):
    albums = get_album()
    profile = get_profile()
    album_count = albums.count()
    context = {
        'profile': profile,
        'album_count': album_count
    }
    return render(request, 'profile-details.html', context)


def add_album(request):
    return album_action(request, CreateAlbumForm, Album(), 'show index', 'add-album.html')


def album_details(request, pk):
    album = Album.objects.get(pk=pk)
    context = {
        'album': album
    }
    return render(request, 'album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    return album_action(request, EditAlbumForm, album, 'show index', 'edit-album.html')


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    return album_action(request, DeleteAlbumForm, album, 'show index', 'delete-album.html')

