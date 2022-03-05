from django.contrib import admin

from exam_2022_02_27.web_app.models import Profile, Album


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username',)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('album_name',)

