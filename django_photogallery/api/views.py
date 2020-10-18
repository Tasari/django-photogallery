from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django_photogallery.models import PicturePost
from django_photogallery.api.serializers import PicturePostSerializer

@api_view(['GET', ])
def api_detail_picturepost_view(request, pk):
    try:
        picture_post = PicturePost.objects.get(pk=pk)
    except PicturePost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PicturePostSerializer(picture_post)
        return Response(serializer.data)