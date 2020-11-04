from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="flight-home"),
    path("<int:flight_id>/",views.flight_det,name="flight_des")
]