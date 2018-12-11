from django.conf.urls import url
from . import views
from django.shortcuts import render

urlpatterns = [url(r'^$', views.index, name='index')]
