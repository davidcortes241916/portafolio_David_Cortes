from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model


class UserSerializers(serializers.ModelSerializer): # muestra usuarios xd
    class Meta:
        model= User
        fields= ['id', 'email', 'name']

#login
User = get_user_model()

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        user = authenticate(username=email, password=password)

        if not user:
            raise serializers.ValidationError("Credenciales inválidas")

        if not user.is_active:
            raise serializers.ValidationError("Usuario inactivo")

        data["user"] = user
        return data