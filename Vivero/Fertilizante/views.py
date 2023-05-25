from django.shortcuts import render
from .forms import crear_fertilizante
from .models import fertilizante

# Create your views here.    
def create_fertilizante(request):
    if request.method == 'GET':
        return render(request, 'crear_fertilizante.html',{
            'form' : crear_fertilizante()
        })
    else:
        fertilizante.objects.create(id_fertilizante = request.POST['id_fertilizante'], nombre_fertilizante = request.POST['nombre_fertilizante'], valor_fertilizante = request.POST['valor_fertilizante'],id_control_plagakey = '')