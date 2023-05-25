from django.shortcuts import render
from .forms import crear_labor
from .models import labor

# Create your views here.
def create_labor(request):
    if request.method == 'GET':
        return render(request, 'crear_labor.html',{
            'form' : crear_labor()
        })
    else:
        labor.objects.create(fecha_labor = request.POST['fecha_labor'], tipo_labor = request.POST['tipo_labor'], descripcion_labor = request.POST['descripcion_labor'],id_viverokey = '')