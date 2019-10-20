from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from .models import CreateNewPage, Tag
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View
from .utils import *


def index(request):
    pre = CreateNewPage.objects.all()
    return render(request, 'index.html', {'pre': pre})


class DetailView(DetailMixin, View):
    model = CreateNewPage
    template = 'page.html'


class DetailTag(DetailMixin, View):
    model = Tag
    template = 'tag.html'


class PageCreate(CreateMixin, View):
    model_form = FormVideo
    template = 'upload_video.html'
    raise_exception = True


class PhotoCreate(CreateMixin, View):
    model_form = FormPhoto
    template = "upload_photo.html"
    raise_exception = True
