from django.conf.urls import url
from . import views
from django.shortcuts import render
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^login/$', views.index, name='index'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/(?P<id>\d+)/$', views.view_profile_with_pk,
        name='view_profile_with_pk'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^profile/password/$', views.change_password, name='change_password'),
    url(r'^profile/reset-password/$',
        password_reset, {
            'template_name': 'reset-password.html',
            'email_template_name': 'reset_password_email.html'
        },
        name='reset_password'),
    url(r'^profile/reset-password/done/$',
        password_reset_done, {'template_name': 'reset-password-done.html'},
        name='password_reset_done'),
    url(r'^profile/reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        password_reset_confirm,
        name='password_reset_confirm'),
    url(r'^profile/reset-password/complete/$',
        password_reset_complete,
        name='password_reset_complete'),
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$',
        views.change_friends,
        name='change_friends')
]
