from .forms import *
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.views.generic import View
from .utils import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def pagenotfound(request, exception):
    return HttpResponseNotFound(render(request, "404.html"))


def index(request):
    pre = CreateNewPage.objects.all()
    return render(request, 'index.html', {'pre': pre})


def photo(request):
    pre = Photo.objects.all()
    return render(request, 'photos.html', {'pre': pre})


class DetailView(DetailMixin, View):
    model = CreateNewPage
    template = 'page.html'


class DetailTag(DetailMixin, View):
    model = Tag
    template = 'tag.html'


class PageCreate(LoginRequiredMixin, CreateMixin, View):
    model_form = FormVideo
    template = 'upload_video.html'
    raise_exception = True


class PhotoCreate(LoginRequiredMixin, CreateMixin, View):
    model_form = FormPhoto
    template = "upload_test.html"
    raise_exception = True


@login_required(login_url='photos')
def create_page(request):
    if request.method == 'POST':
        form = NewPageForm(request.POST, request.FILES)
        if form.is_valid():
            instance = Photo(image=request.FILES['image'],
                             title=request.POST['title'])
            instance.save()
        return HttpResponseRedirect('')
    else:
        form = NewPageForm()
    return render(request, 'upload_photo.html', {'form': form})


@login_required(login_url='photos')
def control(request):
    return render(request, 'control.html')
