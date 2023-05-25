from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('productor', views.create_produtor),
]