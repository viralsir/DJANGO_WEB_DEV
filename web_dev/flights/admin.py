from django.contrib import admin
from .models import airport,flight,Pasenengers

# Register your models here.
admin.site.register(airport)
admin.site.register(flight)
admin.site.register(Pasenengers)