from typing import Any, Dict, Optional

from commons.models import BaseModel
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class CustomUserManager(BaseUserManager):
    def _create_user(
        self,
        username: str,
        email: str,
        password: Optional[str],
        **extra_fields: Dict[str, Any],
    ) -> "CustomUser":

        if not email:
            raise ValueError("The Email must be set")

        email = self.normalize_email(email)

        user = self.model(
            username=username,
            email=email,
            **extra_fields,
        )

        if password is None:
            user.set_unusable_password()
        else:
            user.set_password(password)

        user.full_clean()
        user.save(using=self._db)
        return user

    def create_user(
        self,
        username: str,
        email: str,
        password: Optional[str] = None,
        **extra_fields,
    ):
        extra_fields.setdefault("is_admin", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)

        return self._create_user(
            username=username, email=email, password=password, **extra_fields
        )

    def create_superuser(
        self,
        username: str,
        email: str,
        password: Optional[str] = None,
        **extra_fields,
    ):
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_admin") is not True:
            raise ValueError("Superuser must have is_admin=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(
            username=username, email=email, password=password, **extra_fields
        )


class CustomUser(BaseModel, AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        "username",
        max_length=150,
        unique=True,
    )
    email = models.EmailField(
        "User email",
        max_length=255,
        unique=True,
    )
    is_admin = models.BooleanField(
        "staff status",
        default=False,
    )

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
    objects: CustomUserManager = CustomUserManager()

    def __str__(self) -> str:
        return self.username

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    @property
    def is_staff(self) -> bool:
        return self.is_admin
