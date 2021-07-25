from django.db import models
from taggit.managers import TaggableManager
import os
import random
# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(
        new_filename=new_filename, ext=ext)
    return "Images/{final_filename}".format(
        final_filename=final_filename
    )


class Images(models.Model):
    tags = TaggableManager()
    timestamp = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to=upload_image_path)

    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return str(self.id)

    def get_absolute_image(self):
        return os.path.join('/media', self.image.name)
