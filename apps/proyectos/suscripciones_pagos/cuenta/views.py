from django.shortcuts import render, redirect
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework import generics
from apps.proyectos.suscripciones_pagos.cuenta.models import User
from django.contrib.auth import login as auth_login
from .serializers import LoginSerializer
from django.contrib.auth import logout


#json
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

User = get_user_model()

# VISTAS HTML
def login(request):
    return render(request, "proyectos/pagina_suscripciones/login.html")

def registro(request):
    return render(request, "proyectos/pagina_suscripciones/registro.html")

#registro
@csrf_exempt
def registro_usuario(request):
    print("ENTRÓ A LA VISTA")
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print("DATA RECIBIDA:", data)

            name = data.get("name")
            email = data.get("email")
            password = data.get("password")

            if not name or not email or not password:
                print("error de campos")
                return JsonResponse({"error": "Todos los campos son obligatorios"}, status=400)

            if User.objects.filter(email=email).exists():
                print("error de email")
                return JsonResponse({"error": "Usuario ya existe"}, status=400)

            User.objects.create_user(
                email=email,
                name=name,
                password=password
            )
            print(f"creo usuario: {name}")
            return JsonResponse({"message": "Usuario creado correctamente"}, status=201)

        except Exception as e:
            print(e)
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Método no permitido"}, status=405)

#logout
def logout_view(request):
    logout(request)
    return redirect("cuenta:login") 

# API LOGIN
class LoginUsuarioView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data["user"]

            # Inicia sesión correctamente
            auth_login(request, user)

            return Response(
                {"message": "Login exitoso", "redirect_url": "proyectos/pagina_suscripciones/index.html"},
                status=status.HTTP_200_OK,
                
            )
        print("USER AUTHENTICATED:", request.user.is_authenticated)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )