from django import forms

from exam_2022_02_27.web_app.models import Profile, Album


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age')
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email',
                }
            ),
            'age': forms.TextInput(
                attrs={
                    'placeholder': 'Age',
                }
            )
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name',
                }
            ),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist',
                }
            ),
            'genre': forms.Select(
               choices=Album.CHOICES
            ),
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Description',
                }
            ),
            'image_url': forms.TextInput(
                attrs={
                    'placeholder': 'Image URL',
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'placeholder': 'Price',
                }
            ),
        }


class EditAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name',
                }
            ),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist',
                }
            ),
            'genre': forms.Select(
               choices=Album.CHOICES
            ),
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Description',
                }
            ),
            'image_url': forms.TextInput(
                attrs={
                    'placeholder': 'Image URL',
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'placeholder': 'Price',
                }
            ),
        }


class DeleteAlbumForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'album_name': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                }
            ),
            'artist': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                }
            ),
            'genre': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                }
            ),
            'image_url': forms.TextInput(
                attrs={
                    'readonly': 'Image readonly',
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                }
            ),
        }
