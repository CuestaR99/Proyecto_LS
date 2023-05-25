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
    path('', include('Productor.urls')),
    path('productor/', include('Productor.urls')),
    path('viveros', include('Viveros.urls')),
    path('control/', include('Control.urls')),
    path('fertilizante/', include('Fertilizante.urls')),
    path('hongo/', include('Hongo.urls')),
    path('labor/', include('Labor.urls')),
    
]
