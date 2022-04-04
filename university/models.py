from django.db import models
from django.urls import reverse
from uuid import uuid4
from django.db.models.signals import pre_save


def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    # file_path = "news_archive/{filename}".format(
    #     filename='{}.{}'.format(uuid4().hex, ext))
    file_path = f"news_archive/{uuid4().hex}.{ext}"
    return file_path


class FamousUniversitie(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    country = models.CharField(max_length=100)
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("university:detail-page", args=[str(self.id)])

    @property
    def imageUrl(self):
        try:
            url = str(self.image.url)
        except:
            url = ''
        return url