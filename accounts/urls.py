from django.conf.urls import url
from . import views
from django.shortcuts import render

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^profile/password/$', views.change_password, name='change_password')
]
