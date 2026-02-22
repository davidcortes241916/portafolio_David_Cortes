import stripe
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Pago
from .services import crear_sesion_checkout
from apps.proyectos.suscripciones_pagos.precios_suscripcion.models import Suscripcion
from apps.proyectos.suscripciones_pagos.suscripciones.models import UsuarioSuscripcion


def crear_pago(request, suscripcion_id):
    suscripcion = get_object_or_404(Suscripcion, id=suscripcion_id)

    session = crear_sesion_checkout(request.user, suscripcion)

    # Guardamos pago pendiente
    Pago.objects.create(
        usuario=request.user,
        suscripcion=suscripcion,
        stripe_payment_intent=session.id,
        monto=suscripcion.precio,
        estado="pendiente"
    )

    return redirect(session.url)


def success(request):
    return render(request, "pagos/success.html") #url esta mal cambiarla y crearla plantilla success.html en la carpeta pagos/templates/pagos/success.html


def cancel(request):
    return render(request, "pagos/cancel.html") #igual esta url esta mal cambiarla y crear plantilla cancel.html en la carpeta pagos/templates/pagos/cancel.html

#webhook para recibir notificaciones de Stripe
@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except Exception:
        return HttpResponse(status=400)

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]

        usuario_id = session["metadata"]["usuario_id"]
        suscripcion_id = session["metadata"]["suscripcion_id"]

        pago = Pago.objects.get(stripe_payment_intent=session["id"])
        pago.estado = "exitoso"
        pago.save()

        UsuarioSuscripcion.objects.create(
            usuario_id=usuario_id,
            suscripcion_id=suscripcion_id,
            pagado=True
        )

    return HttpResponse(status=200)