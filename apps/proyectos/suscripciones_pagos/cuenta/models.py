from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    username = None
    email= models.EmailField(unique=True, max_length=254)
    name= models.CharField(max_length=150)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS= ['name']

    def __str__(self):
        return self.email
    