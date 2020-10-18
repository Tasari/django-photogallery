from django.urls import path

from django_photogallery.api.views import api_detail_picturepost_view

app_name = 'photogallery'

urlpatterns = [
    path('<int:pk>/', api_detail_picturepost_view, name="detail"),
]