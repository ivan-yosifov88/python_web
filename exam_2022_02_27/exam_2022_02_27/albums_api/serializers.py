from rest_framework import  serializers

from exam_2022_02_27.web_app.models import Album


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'
