from django import forms


class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class UploadFileForm(forms.Form):
    name = forms.CharField(max_length=20)
    file = forms.FileField()
