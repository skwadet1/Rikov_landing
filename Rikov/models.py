from django.db import models


class preview(models.Model):
    preview_image = models.FileField(upload_to='Rikov/previews/')


class img(models.Model):
    img_source = models.ForeignKey(preview, on_delete=models.CASCADE)
    img_name = models.CharField(max_length=50)
    img_tag = models.CharField(max_length=30)


