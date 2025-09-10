from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'gear/home.html')

def worm_reducer(request):
    return render(request, 'gear/worm_reducer.html')

def worm_one_stage(request):
    return render(request, 'gear/worm_one_stage.html')

def worm_two_stage(request):
    return render(request, 'gear/worm_two_stage.html')

def worm_cylindrical(request):
    return render(request, 'gear/worm_cylindrical.html')

def planetary_reducer(request):
    return render(request, 'gear/planetary_reducer.html')

