from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import FileFieldForm
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic import View


def index(request):
    return render(request, 'index.html')


class FileFieldView(FormView):
    form_class = FileFieldForm
    template_name = 'upload.html'
    success_url = 'index.html'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                ...  # Che to nado s nimi delat'
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
