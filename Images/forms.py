from django import forms
from django.db import models
from .models import Images


class UploadImage(forms.ModelForm):
    model = Images
    fields = ['image', 'tags']
