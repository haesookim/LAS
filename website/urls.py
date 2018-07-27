from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'', views.index),
    url(r'^index/', views.index),
    url(r'^ideals/', views.ideals),
    url(r'^members/', views.members),
    url(r'^projects/', views.projects),
    url(r'^presentations/', views.presentations),
    #may or may not add 'history' page
]
