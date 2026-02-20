from django.shortcuts import render
from apps.proyectos.suscripciones_pagos.precios_suscripcion.models import Suscripcion

# Create your views here.
def index(request):
    suscripciones = Suscripcion.objects.all()
    return render(request, "proyectos/pagina_suscripciones/index.html", {"suscripciones": suscripciones})