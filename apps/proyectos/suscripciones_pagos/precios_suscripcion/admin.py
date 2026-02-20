from django.contrib import admin
from .models import Suscripcion


@admin.register(Suscripcion)
class SuscripcionAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "activa", "fecha_creacion")
    list_filter = ("activa",)
    search_fields = ("nombre",)
