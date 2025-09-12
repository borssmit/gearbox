from django.shortcuts import render

def home(request):
    return render(request, "gear/home.html")

def w1(request):
    return render(request, "gear/w1.html")

def w2(request):
    return render(request, "gear/w2.html")

def cw(request):
    return render(request, "gear/cw.html")

def planetary_reducer(request):
    return render(request, "gear/planetary_reducer.html")

def info(request):
    return render(request, "gear/info.html")

def stub(request):
    return render(request, "gear/stub.html")
