from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    model = User
    ordering = ('email',)

    list_display = ('email', 'name', 'is_staff', 'is_active') #Esto controla qué columnas ves en la lista de usuarios del admin.
    search_fields = ('email', 'name') #Esto permite que el buscador del admin filtre por esos campos.

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = ( #Se usa cuando creas un usuario nuevo desde el admin.
        (None, {
            'classes': ('wide',), #Es configuración visual del formulario en el Django Admin.
            'fields': ('email', 'name', 'password1', 'password2', 'is_staff', 'is_active')
        }),
    )


admin.site.register(User, CustomUserAdmin)