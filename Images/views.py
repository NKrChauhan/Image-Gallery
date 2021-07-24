from django.shortcuts import render
from .models import Images
from django.views.generic import ListView, CreateView
from taggit.models import Tag
import os

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


def EditImage(request, *args, **kwargs):
    pass
