from django.shortcuts import render, redirect
from .forms import crear_ubicacion, crear_vivero
from .models import vivero, ubicacion

# Create your views here.
def create_vivero(request):
    if request.method == 'GET':        
        return render(request, 'vivero_registro.html',{
            'form' : crear_vivero()
        })
    else:
        vivero.objects.create(codigo_vivero = request.POST['codigo_vivero'], nombre_vivero = request.POST['nombre_vivero'], tipo_cultivo= request.POST['tipo_cultivo'])
        return redirect('/productor/')

def create_ubication(request):
    if request.method == 'GET':        
        return render(request, 'ubicacion_vivero.html',{
            'form' : crear_ubicacion()
        })
    else:
        ubicacion.objects.create(departemento = request.POST['departemento'], municipio = request.POST['municipio'], vereda= request.POST['vereda'])