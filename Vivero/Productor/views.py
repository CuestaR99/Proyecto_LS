from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import crear_productor
from .models import productor

def create_produtor(request):
    if request.method == 'GET':
        return render(request, 'productor_nuevo.html',{
            'form' : crear_productor()
        })
    else:        
        productor.objects.create(Cedula = request.POST['Cedula'], Nombre = request.POST['Nombre'], Apellido = request.POST['Apellido'], Telefono = request.POST['Telefono'], Correo = request.POST['Correo'])        
        redirect(login)

def login(request):
    return render(request, 'inicio_page.html')