from django import forms

from exam_prep.online_lib.models import Book, Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image_url')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Full Name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name',
                }
            ),
            'image_url': forms.TextInput(
                attrs={
                    'placeholder': 'URL',
                }
            )
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                }
            ),
            'image_url': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                }
            )
        }


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'description', 'image', 'type')
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Title',
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Description',
                }
            ),
            'image': forms.TextInput(
                attrs={
                    'placeholder': 'Image',
                }
            ),
            'type': forms.TextInput(
                attrs={
                    'placeholder': 'Fiction, Novel, Crime...',
                }
            )
        }


class EditBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'description', 'image', 'type')




