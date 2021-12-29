from accounts.models import CustomUser


def create_user(*, username, email, password, **extra_fields):
    user = CustomUser.objects.create_user(
        username=username,
        email=email,
        password=password,
        **extra_fields,
    )
    return user
