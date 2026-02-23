from django.shortcuts import render
from apps.proyectos.suscripciones_pagos.precios_suscripcion.models import Suscripcion
from apps.proyectos.suscripciones_pagos.suscripciones.models import UsuarioSuscripcion
from django.utils import timezone


# Create your views here.

def index(request):
    suscripciones = Suscripcion.objects.all()
    suscripcion_usuario = None

    if request.user.is_authenticated:
        suscripcion_usuario = UsuarioSuscripcion.objects.filter(
            usuario=request.user,
            estado='activa',
            fecha_vencimiento__gt=timezone.now()
        ).select_related("suscripcion").first()

    return render(request, "proyectos/pagina_suscripciones/index.html", {
        "suscripciones": suscripciones,
        "suscripcion_usuario": suscripcion_usuario,
    })