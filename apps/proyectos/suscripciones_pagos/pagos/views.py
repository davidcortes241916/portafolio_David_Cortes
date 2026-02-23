import stripe
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Pago
from .services import crear_sesion_checkout
from apps.proyectos.suscripciones_pagos.precios_suscripcion.models import Suscripcion
from apps.proyectos.suscripciones_pagos.suscripciones.models import UsuarioSuscripcion
from django.utils import timezone
from datetime import timedelta


def success(request):
    session_id = request.GET.get("session_id")

    if not session_id:
        return redirect("precios_suscripcion:index")

    session = stripe.checkout.Session.retrieve(session_id)

    usuario_id = session["metadata"]["usuario_id"]
    suscripcion_id = session["metadata"]["suscripcion_id"]

    UsuarioSuscripcion.objects.update_or_create(
        usuario_id=usuario_id,
        defaults={
            "suscripcion_id": suscripcion_id,
            "estado": "activa",
            "pagado": True,
            "fecha_vencimiento": timezone.now() + timedelta(days=30)
        }
    )

    return render(request, "proyectos/pagina_suscripciones/success.html")


def cancel(request):
    return render(request, "proyectos/pagina_suscripciones/cancel.html") 

#json respuesta para crear pago desde frontend con fetch
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .services import crear_sesion_checkout
from .models import Suscripcion

@login_required
def crear_pago(request, suscripcion_id):

    if not request.user.is_authenticated:
        return JsonResponse(
            {"error": "Debes iniciar sesión para suscribirte."},
            status=401
        )

    suscripcion = Suscripcion.objects.get(id=suscripcion_id)
    session = crear_sesion_checkout(request.user, suscripcion)

    return JsonResponse({"sessionId": session.id})

#webhook para recibir notificaciones de Stripe
@csrf_exempt
def stripe_webhook(request):
    print("🔥 WEBHOOK RECIBIDO")

    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")

    if not sig_header:
        print("❌ No signature header")
        return HttpResponse(status=400)

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except Exception as e:
        print("❌ Error verificando webhook:", e)
        return HttpResponse(status=400)

    print("✅ Evento recibido:", event["type"])

    return HttpResponse(status=200)