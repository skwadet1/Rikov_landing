from django import forms
from .models import *
from django.core.exceptions import ValidationError


class NewPageForm(forms.Form):
    title = forms.CharField(max_length=30)
    image = forms.FileField()


class FormVideo(forms.ModelForm):
    class Meta:
        model = CreateNewPage
        fields = ['title', 'slug', 'embedded_url', 'preview_image', 'tag']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'embedded_url': forms.TextInput(attrs={'class': 'form-control'}),
            'preview_image': forms.FileInput(attrs={'class': 'form-control'}),
            'tag': forms.SelectMultiple(attrs={'class': 'form-control'})
        }


class FormPhoto(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

