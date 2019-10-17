from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import FileFieldForm, UploadFileForm
from .models import preview
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic import View


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = preview(preview_image=request.FILES['file'])
            instance.save()
            return HttpResponseRedirect('/index/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def index(request):
    pre = preview.objects.all()
    return render(request, 'index.html', {'pre': pre})
