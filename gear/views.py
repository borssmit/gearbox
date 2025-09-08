from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, '/home/bors/django_projects/gearbox/gear/templates/gear/home.html')