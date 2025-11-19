from django.contrib import admin
from .models import Empleado, Cliente, Atraccion

# Registrar los tres modelos
admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(Atraccion)