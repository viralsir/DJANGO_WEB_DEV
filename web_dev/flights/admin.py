from django.contrib import admin
from .models import airport,flight,Pasenengers

class FlightAdmin(admin.ModelAdmin):
    list_display = ("origin","destion","duration")


class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

# Register your models here.
admin.site.register(airport)
admin.site.register(flight,FlightAdmin)
admin.site.register(Pasenengers,PassengerAdmin)