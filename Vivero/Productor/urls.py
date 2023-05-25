from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login_in"),
    path('productor', views.create_produtor),
]