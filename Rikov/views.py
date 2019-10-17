from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import UploadFileForm, NewPageForm
from .models import preview, CreateNewPage
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View


def create_page(request):
    if request.method == 'POST':
        form = NewPageForm(request.POST, request.FILES)
        if form.is_valid():
            instance = CreateNewPage(preview_image=request.FILES['file'], tag=request.POST['tag'],
                                     title=request.POST['title'], url=request.POST['url'], embedded_url=request.POST['embedded_url'])
            instance.save()
            return HttpResponseRedirect('/index/')
    else:
        form = NewPageForm()
    return render(request, 'create.html', {'form': form})


def index(request):
    pre = CreateNewPage.objects.all()
    return render(request, 'index.html', {'pre': pre})
