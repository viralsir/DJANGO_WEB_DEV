from django.shortcuts import render
from .models import flight

# Create your views here.
def index(request):
    return render(request,"flights/index.html",{
        "flights":flight.objects.all()
    })

def flight_det(request,flight_id):
    flight_details=flight.objects.get(pk=flight_id)

    return render(request,"flights/flight_details.html",{
        "flight":flight_details,
        "passengers":flight_details.passengers.all()
    })