from django.shortcuts import render, get_object_or_404

# Create your views here.
from Autos.models import Auto


def detalleAuto(request,id):
    Vehiculo = get_object_or_404(Auto, pk=id)
    return render (request, 'Autos/Caracteristicas.html',{'Detalle': Vehiculo})
