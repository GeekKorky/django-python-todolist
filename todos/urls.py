from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^details/(?P<id>\d+)/$', views.details),
    url(r'^details/edit/(?P<id>\d+)/$', views.edit, name='edit'),
    url(r'^details/delete/(?P<id>\d+)/$', views.delete, name='delete'),
    url(r'^add', views.add, name='add'),
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'logout.html'}, name='logout'),
    url(r'^register/$', views.register, name='register')
]
