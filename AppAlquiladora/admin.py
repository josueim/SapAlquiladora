from django.contrib import admin
from .models import Vehiculos, PersonalVehiculos, GestionMobiliaria, Personal, MenusComida, Clientes, Historial, Presupuesto

# Register your models here.
admin.site.register(Vehiculos)
admin.site.register(PersonalVehiculos)
admin.site.register(GestionMobiliaria)
admin.site.register(Personal)
admin.site.register(MenusComida)
admin.site.register(Clientes)
admin.site.register(Historial)
admin.site.register(Presupuesto)