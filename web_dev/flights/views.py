from django.shortcuts import render
from .models import flight

# Create your views here.
def index(request):
    return render(request,"flights/index.html",{
        "flights":flight.objects.all()
    })