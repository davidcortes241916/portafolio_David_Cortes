from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, "proyectos/pagina_suscripciones/login.html")

def index(request):
    return render(request, "proyectos/pagina_suscripciones/index.html")

def registro(request):
    return render(request, "proyectos/pagina_suscripciones/registro.html")