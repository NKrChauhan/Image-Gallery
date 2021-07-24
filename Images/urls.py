from django.urls import path
from .views import TagView, HomeView, UploadImage, EditImage, rotate_image_colockwise
app_name = 'images'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('edit/<int:id>/', EditImage, name='edit'),
    path('upload/', UploadImage.as_view(), name='upload'),
    path('tag/<slug:tag>/', TagView.as_view(), name='images_by_tags'),
    path('rotateC/<int:id>/', rotate_image_colockwise, name='clockRotation'),
]
