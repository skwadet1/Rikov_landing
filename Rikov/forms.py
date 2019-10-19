from django import forms


class NewPageForm(forms.Form):
    title = forms.CharField(max_length=30)
    url = forms.SlugField(max_length=100)
    embedded_url = forms.URLField(max_length=200)
    tag = forms.SlugField(max_length=50)
    file = forms.FileField()
