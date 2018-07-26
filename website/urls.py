from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.ideals, name = 'ideals'),
    url(r'^$', views.members, name='members'),
    url(r'^$', views.projects, name='projects'),
    url(r'^$', views.presentations, name='presentations'),
    #may or may not add 'history' page
]
