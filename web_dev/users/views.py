from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def home(request):
    if not request.user.is_authenticated :
        return HttpResponseRedirect(reverse('login'))
    else :
        return render(request,"users/usr.html")

def loginview(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        user=authenticate(request,username=username,password=password)

        if user is not None :
            login(request,user)
            return HttpResponseRedirect(reverse("user-home"))
        else :
            return render(request,"users/login.html",{
                "message":"invalid  username or password"
            })
    return render(request,"users/login.html")

def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

