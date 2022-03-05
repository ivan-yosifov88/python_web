from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from exam_2022_02_27.albums_api.serializers import AlbumSerializer
from exam_2022_02_27.web_app.models import Album


class ListAlbumsView(APIView):
    def get(self, request):
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response({"albums": serializer.data})

    def post(self, request):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
