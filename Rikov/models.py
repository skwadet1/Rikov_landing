from django.db import models
from django.shortcuts import reverse


class CreateNewPage(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=100, unique=True)
    tag = models.ManyToManyField('Tag', blank=True, related_name='pages')
    embedded_url = models.URLField(max_length=200)
    preview_image = models.FileField(upload_to='previews/')

    def get_absolute_url(self):
        return reverse('pages_url', kwargs={'slug': self.slug})

    def _str_(self):
        return '{}'.format(self.title)


class Tag(models.Model):
    title = models.CharField(max_length=50, default='Photo')
    slug = models.SlugField(max_length=50)

    def get_absolute_url(self):
        return reverse('tag_url', kwargs={'slug': self.slug})

    def _str_(self):
        return '{}'.format(self.title)


class Photo(models.Model):
    title = models.CharField(max_length=50)
    image = models.FileField(upload_to='photos/')

    def _str_(self):
        return '{}'.format(self.title)
