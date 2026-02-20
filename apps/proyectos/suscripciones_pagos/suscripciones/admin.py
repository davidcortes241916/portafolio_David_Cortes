from django.contrib import admin
from .models import UsuarioSuscripcion

@admin.register(UsuarioSuscripcion)
class UsuarioSuscripcionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'suscripcion', 'estado', 'pagado', 'fecha_vencimiento')