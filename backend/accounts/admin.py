from typing import Any

from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.http.request import HttpRequest

from accounts.models import CustomUser
from accounts.services import user_create

# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = (
        "username",
        "email",
        "is_admin",
        "is_superuser",
        "is_active",
        "created_at",
        "updated_at",
    )
    # Filtro de pesquisa
    search_fields = ("email", "username")
    # Filtro clicavel
    list_filter = ("is_active", "is_admin", "is_superuser")

    # Campos formulario para criação de um
    fieldsets = (
        ("Info", {"fields": ("username", "email", "password")}),
        ("Permissions", {"fields": ("is_admin", "is_active")}),
    )
    # Cria campo para criação de usuario???? Talvez
    add_fieldsets = (
        (
            "Info",
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "is_admin",
                    "is_active",
                ),
            },
        ),
    )

    def save_model(
        self, request: HttpRequest, obj: CustomUser, form: ModelForm, change: bool
    ) -> None:
        if change:
            return super().save_model(request, obj, form, change)
        try:
            user_create(**form.cleaned_data)
        except ValidationError as exc:
            self.message_user(request, str(exc), messages.ERROR)
