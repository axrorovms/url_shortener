from django.urls import path
from .views import home, createShortUrl, redirect

urlpatterns = [
    path('', home, name='home'),
    path('create/', createShortUrl, name='create'),
    path('<str:url>', redirect, name='redirect'),
]
