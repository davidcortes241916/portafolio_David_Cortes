from django.urls import path
from apps.proyectos.suscripciones_pagos.cuenta import views
from .views import LoginUsuarioView

app_name = "cuenta"

urlpatterns = [
    #login
    path("login/", views.login, name="login"),
    path("login_usuario/", LoginUsuarioView.as_view(), name="login_usuario"),
    #registro
    path("registro/", views.registro, name="registro"),
    path("registro_usuario/", views.registro_usuario, name="registro_usuario"),
    #logout
    path("logout/", views.logout_view, name="logout"),
]