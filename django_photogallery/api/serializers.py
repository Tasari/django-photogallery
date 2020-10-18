from rest_framework import serializers

from django_photogallery.models import PicturePost

class PicturePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PicturePost
        fields = ['name', 'description', 'pub_date', 'source', 'picture', 'url_height', 'url_width']