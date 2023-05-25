from django.urls import path
from . import views

urlpatterns = [
    path('', views.crear_control),
    path('plaga/', views.crear_control_plaga),
    
]