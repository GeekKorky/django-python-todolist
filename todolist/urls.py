from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    #url(r'^$', include('todos.urls')),
    url(r'^todos/', include('todos.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^admin/', admin.site.urls)
]
