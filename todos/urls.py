from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^details/(?P<id>\d+)/$', views.details),
    #url(r'^details/edit/(?P<pk>\d+)/$', views.edit, name='edit'),
    url(r'^add', views.add, name='add'),
    url(r'^login/$', login, {'template_name': 'login.html'}),
    url(r'^logout/$', logout, {'template_name': 'logout.html'}),
    url(r'^register/$', views.register, name='register')
]
