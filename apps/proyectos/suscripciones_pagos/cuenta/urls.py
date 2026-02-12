from django.urls import path
from apps.proyectos.suscripciones_pagos.cuenta import views
app_name= "cuenta"

urlpatterns = [
    path("index/", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("registro/", views.registro, name="registro"),
]