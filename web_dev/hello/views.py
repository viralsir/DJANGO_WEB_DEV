from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hello world !")

def vimal(request):
    return HttpResponse("Hello Vimal !")

def amit(request):
    return HttpResponse("Hello Amit !")

def greetings(request,name):
   # return HttpResponse(f"Hello {name.upper()} !")
    return render(request,"hello\home.html",{'name':name})
