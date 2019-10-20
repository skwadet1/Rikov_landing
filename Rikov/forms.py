from django import forms
from .models import *
from django.core.exceptions import ValidationError


class NewPageForm(forms.Form):
    title = forms.CharField(max_length=30)
    url = forms.SlugField(max_length=100)
    embedded_url = forms.URLField(max_length=200)
    tag = forms.SlugField(max_length=50)
    file = forms.FileField()


class FormVideo(forms.ModelForm):
    class Meta:
        model = CreateNewPage
        fields = ['title', 'slug', 'embedded_url', 'tag', 'preview_image']

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
