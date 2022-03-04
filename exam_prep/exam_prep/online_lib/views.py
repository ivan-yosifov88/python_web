from django.shortcuts import redirect, render

from exam_prep.online_lib.forms import CreateProfileForm, DeleteProfileForm, EditProfileForm
from exam_prep.online_lib.models import Book, Profile


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def get_books():
    books = Book.objects.all()
    if books:
        return books
    return None


def show_index(request):
    profile = get_profile()
    books = get_books()
    if not profile:
        return redirect('create profile')

    context = {
        'books': books
    }
    return render(request, 'home-with-profile.html', context)


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


def create_profile(request):
    return profile_action(request, CreateProfileForm, Profile(), 'show index', 'home-no-profile.html')


def show_profile(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'profile.html', context)


def edit_profile(request):
    return profile_action(request, EditProfileForm, get_profile(), 'show index', 'edit-profile.html')


def profile_delete(request):
    return profile_action(request, DeleteProfileForm, get_profile(), 'show index', 'delete-profile.html')


def create_book(request):
    return render(request, 'add-book.html')


def edit_book(request, pk):
    return render(request, 'edit-book.html')


def book_details(request, pk):
    return render(request, 'book-details.html')
