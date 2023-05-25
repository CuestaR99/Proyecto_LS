from django.shortcuts import render
from .forms import crear_hongo
from .models import hongo

# Create your views here.
def create_hongo(request):
    if request.method == 'GET':
        return render(request, 'crear_fertilizante.html',{
            'form' : crear_hongo()
        })
    else:
        hongo.objects.create(id_hongo = request.POST['id_hongo'], nombre_hongo = request.POST['nombre_hongo'], tipo_hongo = request.POST['tipo_hongo'],id_control_plagakey = '')
