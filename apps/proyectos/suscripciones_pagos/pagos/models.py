from django.db import models
from django.conf import settings
from apps.proyectos.suscripciones_pagos.precios_suscripcion.models import Suscripcion


class Pago(models.Model):

    ESTADOS = (
        ('pendiente', 'Pendiente'),
        ('exitoso', 'Exitoso'),
        ('fallido', 'Fallido'),
    )

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    suscripcion = models.ForeignKey(Suscripcion, on_delete=models.CASCADE)

    stripe_payment_intent = models.CharField(max_length=255, blank=True, null=True)

    monto = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')

    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} - {self.estado}"
