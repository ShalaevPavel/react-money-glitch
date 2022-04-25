from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Marks
from django_admin_geomap import geomap_context
from .models import Location
from .forms import CreateNewMark



def index(request):
    return HttpResponse("I can't breath")

# Create your views here.

class MarksDetailView(DetailView):
    model = Marks
    template_name = 'marks.html'

def some_test(response):
    return render(response, "root.html", {"inside_var":"smth"})

def site_func(response):
    return render(response, "marks.html", {"my_var" : "var"})

def default_map(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'default.html',
                  { 'mapbox_access_token': mapbox_access_token })


def marks_create(request):
    if request.POST:
        form1 = CreateNewMark
        form1.is_valid()
        form1.save()
    return render(request, 'marks_form.html', context={'form1': CreateNewMark})

def home(request):
    return render(request, 'home.html', geomap_context(Location.objects.all()))