from django.http import HttpResponse
from django.shortcuts import render


from Autos.models import Auto


# Create your views here.
def SelectCar(request):
    No_Vehiculo = Auto.objects.count()
    Vehiculo = Auto.objects.all()
    # return render(request,"bienvenido.html",{'msg1': 'valor mensaje 1', 'msg2': 'valor mensje 2'} )
    return render(request, "Bienvenido.html", {'Cantidad': No_Vehiculo, 'Detalle': Vehiculo})








from django.shortcuts import render

# Create your views here.
