from django.db import models


class CreateNewPage(models.Model):
    title = models.CharField(max_length=30)
    url = models.CharField(max_length=200)
    embedded_url = models.URLField(max_length=200)
    tag = models.CharField(max_length=15)
    preview_image = models.FileField(upload_to='previews/')
