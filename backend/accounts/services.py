from typing import Any, Dict

from accounts.models import CustomUser


def user_create(
    *, username, email, password, **extra_fields: Dict[str, Any]
) -> CustomUser:
    user = CustomUser.objects.create_user(
        username=username,
        email=email,
        password=password,
        **extra_fields,
    )

    return user
