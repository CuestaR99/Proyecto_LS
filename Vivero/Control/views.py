from django.shortcuts import render ,redirect
from .forms import control_viveros, control_plaga
from .models import control, Control_Plaga

# Create your views here.
def crear_control(request):
    if request.method == 'GET':
        return render(request, 'crear_control.html',{
        'form': control_viveros()
    })
    else:
        control.objects.create(tipo_control = request.POST['tipo_control'], nombre_control = request.POST['nombre_control'], id_laborkey=1)
        return redirect('')



def crear_control_plaga(request):
    if request.method == 'GET':        
        return render(request, 'crear_control_plaga.html',{
        'form': control_plaga()
    })
    else:
        Control_Plaga.objects.create(periodo_carencia = request.POST['periodo_carencia'], registro_ica = request.POST['registro_ica'], frecuencia_aplicacion = request.POST['frecuencia_aplicacion'], id_controlkey = 1)