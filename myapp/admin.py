from django.contrib import admin
from .models import Clientes, Medicos

# Register your models here. panel de administrador
admin.site.register(Clientes)
admin.site.register(Medicos)
