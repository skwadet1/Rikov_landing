from django.db import models


class img(models.Model):
    img_source = models.CharField(max_length=100)
    img_name = models.CharField(max_length=50)
    img_tag = models.CharField(max_length=30)
