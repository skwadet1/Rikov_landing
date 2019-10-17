from django import forms


class NewPageForm(forms.Form):
    title = forms.CharField(max_length=30)
    url = forms.URLField(max_length=200)
    embedded_url = forms.CharField(max_length=200)
    tag = forms.CharField(max_length=15)
    file = forms.FileField()
