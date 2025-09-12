"""
URL configuration for gearbox project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gear import views
urlpatterns = [
    path("", views.home, name="home"),
    path("w1/", views.w1, name="w1"),
    path("w2/", views.w2, name="w2"),
    path("cw/", views.cw, name="cw"),
    path("planetary/", views.planetary_reducer, name="planetary"),
    path("info/", views.info, name="info"),
    path("stub/", views.stub, name="stub"),
]
