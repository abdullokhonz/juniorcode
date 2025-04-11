from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('robots.txt', views.robots_txt, name='robots_txt')
]
