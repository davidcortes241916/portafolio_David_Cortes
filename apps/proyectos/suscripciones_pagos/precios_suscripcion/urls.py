from django.urls import path, include
from apps.proyectos.suscripciones_pagos.precios_suscripcion import views

app_name= 'precios_suscripcion'

urlpatterns = [
    path("", views.index, name="index"),
]