from django.urls import path
from apps.portafolio import views

app_name= 'portafolio'

urlpatterns = [
    path("", views.index, name="inicio"),
]