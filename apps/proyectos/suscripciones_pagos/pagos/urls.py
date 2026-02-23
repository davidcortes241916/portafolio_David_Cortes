from django.urls import path
from . import views
from .views import stripe_webhook

app_name = "pagos"

urlpatterns = [
    path("crear/<int:suscripcion_id>/", views.crear_pago, name="crear_pago"),
    path("success/", views.success, name="success"),
    path("cancel/", views.cancel, name="cancel"),
    path("webhook/", views.stripe_webhook, name="webhook"),
    path("stripe-webhook/", stripe_webhook, name="stripe_webhook"),
]