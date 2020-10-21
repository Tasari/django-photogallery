from django.urls import path

from django_photogallery.api.views import (
    api_detail_picturepost_view,
    api_update_picturepost_view,
    api_post_picturepost_view,
    api_delete_picturepost_view,
)
app_name = 'photogallery'

urlpatterns = [
    path('<int:pk>/', api_detail_picturepost_view, name="detail"),
    path('<int:pk>/update', api_update_picturepost_view, name="update"),
    path('<int:pk>/delete', api_delete_picturepost_view, name="delete"),
    path('create', api_post_picturepost_view, name="create"),
]