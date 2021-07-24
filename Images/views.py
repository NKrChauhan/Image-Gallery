from django.shortcuts import redirect, render
from .models import Images
from django.views.generic import ListView, CreateView
from taggit.models import Tag
import os
from PIL import Image

# Create your views here.


class TagsMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagsMixin, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class TagView(TagsMixin, ListView):
    model = Images
    template_name = 'Images/home.html'
    context_object_name = 'images'

    def get_queryset(self):
        return Images.objects.filter(tags__slug=self.kwargs.get('tag'))


class HomeView(TagsMixin, ListView):
    model = Images
    template_name = 'Images/home.html'
    queryset = Images.objects.all()
    context_object_name = 'images'


class UploadImage(CreateView):
    model = Images


def rotate_image_colockwise(request, id, *args, **kwargs):
    object = Images.objects.filter(id=id)
    data = {
        'img_obj': "not found",
    }
    if object:
        object = object.first()
        image = Image.open(object.image.path)
        r_image = image.rotate(90)
        object.image = r_image
        object.save(commit=True)
    return redirect(EditImage, id=id)


def EditImage(request, id, *args, **kwargs):
    object = Images.objects.filter(id=id)
    data = {
        'img_obj': "not found",
    }
    if object:
        data = {
            'img_obj': object.first(),
        }
    return render(request=request, template_name='Images/edit-image.html', context=data)
