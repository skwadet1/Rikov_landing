from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import FormView
from .forms import NewPageForm
from .models import CreateNewPage, Tag
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View
from .utils import DetailMixin


def create_page(request):
    if request.method == 'POST':
        form = NewPageForm(request.POST, request.FILES)
        if form.is_valid():
            instance = CreateNewPage(preview_image=request.FILES['file'],
                                     title=request.POST['title'], slug=request.POST['url'],
                                     embedded_url=request.POST['embedded_url'])
            instance.save()
            return HttpResponseRedirect('/index/')
    else:
        form = NewPageForm()
    return render(request, 'create.html', {'form': form})


def index(request):
    pre = CreateNewPage.objects.all()
    return render(request, 'index.html', {'pre': pre})


class DetailView(DetailMixin, View):
    model = CreateNewPage
    template = 'page.html'


class DetailTag(DetailMixin, View):
    model = Tag
    template = 'tag.html'


