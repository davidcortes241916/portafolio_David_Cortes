from django.db import models
from apps.proyectos.suscripciones_pagos.precios_suscripcion.models import Suscripcion
from datetime import timedelta
from django.utils import timezone
from django.conf import settings

class UsuarioSuscripcion(models.Model):
    ESTADOS = (
        ('activa', 'Activa'),
        ('vencida', 'Vencida'),
        ('cancelada', 'Cancelada'),
    )

    usuario = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE
    )
    suscripcion = models.ForeignKey(Suscripcion, on_delete=models.CASCADE)

    fecha_inicio = models.DateTimeField(default=timezone.now)
    fecha_vencimiento = models.DateTimeField()

    estado = models.CharField(max_length=20, choices=ESTADOS, default='activa')
    pagado = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Si no tiene fecha de vencimiento la calculamos
        if not self.fecha_vencimiento:
            self.fecha_vencimiento = self.fecha_inicio + timedelta(days=30)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.usuario.username} - {self.suscripcion.nombre}"