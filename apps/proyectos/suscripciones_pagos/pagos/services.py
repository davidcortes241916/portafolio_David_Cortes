import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


def crear_sesion_checkout(usuario, suscripcion):
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        mode="payment",
        customer_email=usuario.email,
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {
                        "name": suscripcion.nombre,
                        "description": suscripcion.descripcion,
                    },
                    "unit_amount": int(suscripcion.precio * 100),
                },
                "quantity": 1,
            }
        ],
        success_url="http://127.0.0.1:8000/pagos/success/?session_id={CHECKOUT_SESSION_ID}",
        cancel_url="http://127.0.0.1:8000/pagos/cancel/",
        metadata={
            "usuario_id": usuario.id,
            "suscripcion_id": suscripcion.id,
        }
    )

    return session