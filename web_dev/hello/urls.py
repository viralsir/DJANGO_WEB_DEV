from django.urls import  path
from . import views

urlpatterns=[
    path("",views.index,name="home"),
    path("vimal",views.vimal,name="vimal"),
    path("amit",views.amit,name="amit"),
    path("greetings/<str:name>",views.greetings,name="greet")

]