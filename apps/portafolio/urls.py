from django.urls import path
from apps.portafolio import views

app_name= 'portafolio'

urlpatterns = [
    path("", views.index, name="inicio"),
    path("contacto/", views.contact, name="contacto"),
    path("respuesta/", views.contact_ajax, name="contact_ajax"),
    path("proyectos/", views.projects, name="proyectos"),
    path("resumen/", views.resumen, name="resumen"),
    #descargar CV
    path('download-cv/', views.download_cv, name='download_cv'),
]