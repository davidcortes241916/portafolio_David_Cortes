from django.urls import path
from apps.proyectos.suscripciones_pagos.precios_suscripcion import views
app_name= 'apps.proyectos.suscripciones_pagos.precios_suscripcion'

urlpatterns = [
    path("", views.index, name="inicio"),
]