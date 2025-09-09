from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, '/home/bors/django_projects/gearbox/gear/templates/gear/home.html')

def worm_reducer(request):
    return render(request, '/home/bors/django_projects/gearbox/gear/templates/gear/worm_reducer.html')

def planetary_reducer(request):
    return render(request, '/home/bors/django_projects/gearbox/gear/templates/gear/planetary_reducer.html')

