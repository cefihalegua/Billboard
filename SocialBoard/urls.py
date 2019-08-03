from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout

from . import views
#app_name = 'socialboard'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, kwargs={'next_page': '/social'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^newpost$', views.newpost, name='newpost')
]
