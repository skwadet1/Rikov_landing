from django import forms


class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class UploadFileForm(forms.Form):
    name = forms.CharField(max_length=20)
    file = forms.FileField()


class CreateNewPage(forms.Form):
    title = forms.CharField(max_length=30)
    url = forms.URLField(max_length=200)
    tag = forms.CharField(max_length=15)
    preview_path = forms.CharField(max_length=30)
