from django.urls import path
from . import views



urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('about', views.about),
    path('help', views.help),
]