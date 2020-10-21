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

@api_view(['PUT', ])
def api_update_picturepost_view(request, pk):
    try:
        picture_post = PicturePost.objects.get(pk=pk)
    except PicturePost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = PicturePostSerializer(picture_post, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update success"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE', ])
def api_delete_picturepost_view(request, pk):
    try:
        picture_post = PicturePost.objects.get(pk=pk)
    except PicturePost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        operation = picture_post.delete()
        data = {}
        if operation:
            data["success"] = "delete success"
        else:
            data["fail"] = "delete failed"
        return Response(data=data)

@api_view(['POST', ])
def api_post_picturepost_view(request):
    picture_post = PicturePost()

    if request.method == "POST":
        serializer = PicturePostSerializer(picture_post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
