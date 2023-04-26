
from django.urls import path
from . import views






urlpatterns = [
    path('', views.index),
    path('search', views.search),
    path('<slug:slug>', views.details, name="subscriptions_details"),
    path('category/<slug:slug>', views.getSubscriptionsByCategory, name='subscriptions_by_category'),
]