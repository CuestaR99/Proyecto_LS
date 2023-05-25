from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_vivero, name='crear_vivero'),
    path('ubicacion/', views.create_ubication),
]