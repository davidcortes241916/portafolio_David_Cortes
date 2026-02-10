from django.shortcuts import render
from django.http import FileResponse, Http404
import os
from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse


# Create your views here.
def index(request):
    return render(request, "portafolio/index.html")

def contact(request):
    return render(request, "portafolio/contact.html")

def contact_ajax(request):

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if not name or not email or not message:
            return JsonResponse({
                "success": False,
                "error": "Todos los campos son obligatorios"
            })

        send_mail(
            subject="Nuevo mensaje desde tu portafolio",
            message=f"Nombre: {name}\nCorreo: {email}\n\nMensaje:\n{message}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=["davidalejandro241916@gmail.com"],
        )

        return JsonResponse({"success": True})

    return JsonResponse({"success": False}, status=400)

def projects(request):
    return render(request, "portafolio/projects.html")

def resumen(request):
    return render(request, "portafolio/resumen.html")

#descargar CV
def download_cv(request):
    file_path = os.path.join(
        settings.BASE_DIR,
        'static',
        'docs',
        'CV_Desarrollador_Backend_Junior_David_Cortes.pdf'
    )

    if not os.path.exists(file_path):
        raise Http404("El archivo no existe")

    return FileResponse(open(file_path, 'rb'), as_attachment=True)