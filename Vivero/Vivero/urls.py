"""
URL configuration for Vivero project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', include('Productor.urls'), name="index"),
    path('productor/', include('Productor.urls'), name="productor_"),
    path('viveros/', include('Viveros.urls'), name="viveros_"),
    path('control/', include('Control.urls'), name="control_"),
    path('fertilizante/', include('Fertilizante.urls'), name="fertilizante_"),
    path('hongo/', include('Hongo.urls'), name="hongo_"),
    path('labor/', include('Labor.urls'), name="labor_"),
    
]
