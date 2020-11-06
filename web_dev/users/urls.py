from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name="user-home"),
    path("login",views.loginview,name="login"),
    path("logout",views.logoutview,name="logout")

]