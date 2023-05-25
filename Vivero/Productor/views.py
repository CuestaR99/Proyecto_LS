from django.shortcuts import render, redirect
from .forms import crear_productor
from .models import productor

def create_produtor(request):
    if request.method == 'GET':
        return render(request, 'productor_nuevo.html',{
            'form' : crear_productor()
        })
    else:
        print(request.POST)
        productor.objects.create(cedula = request.POST['cedula'], nombre = request.POST['nombre'], apellido = request.POST['apellido'], telefono = request.POST['telefono'], correo = request.POST['correo'])
        redirect('index')

def login(request):
    return render(request, 'inicio_page.html')