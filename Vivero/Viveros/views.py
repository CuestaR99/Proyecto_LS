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
        vivero.objects.create(Codigo_vivero = request.POST['Codigo_vivero'], Nombre_vivero = request.POST['Nombre_vivero'], Tipo_cultivo= request.POST['Tipo_cultivo'],id_productor_id='')
        return redirect('/productor/')

def create_ubication(request):
    if request.method == 'GET':        
        return render(request, 'ubicacion_vivero.html',{
            'form' : crear_ubicacion()
        })
    else:
        ubicacion.objects.create(Departemento = request.POST['Departemento'], Municipio = request.POST['Municipio'], Vereda= request.POST['Vereda'])