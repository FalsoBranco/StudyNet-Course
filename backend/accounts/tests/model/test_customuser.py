import pytest
from accounts.models import CustomUser
from django.core.exceptions import ValidationError

pytestmark = pytest.mark.django_db


@pytest.fixture
def user_info():
    return {
        "username": "FalsoBranco",
        "email": "falso_branco@gmail.com",
    }


class TestModelBaseUser:
    def test_create_user(self, user_info):
        user: CustomUser = CustomUser.objects.create_user(**user_info)
        assert user.pk == user.id

    def test_create_superuser(self, user_info):
        superuser: CustomUser = CustomUser.objects.create_superuser(**user_info)
        assert superuser.is_staff is True

    def test_user_without_password_is_created_with_unusable_one(self, user_info):
        user: CustomUser = CustomUser.objects.create_user(**user_info)
        assert user.has_usable_password() is False

    def test_user_with_password_is_created_with_usable_one(self, user_info):
        user: CustomUser = CustomUser.objects.create_user(
            **user_info, password="falsobranco24"
        )
        assert user.has_usable_password() is True

    def test_user_with_capitalized_email_cannot_be_created(self, user_info):
        message: str = "Shoud be created one user, skiping capitalized email"
        CustomUser.objects.create_user(**user_info)

        with pytest.raises(ValidationError):
            user_info["email"] = "FALSO_BRANCO@gmail.com"
            CustomUser.objects.create_user(**user_info)

        assert CustomUser.objects.count() == 1, message

    def test_superuser_without_admin_cannot_be_created(self, user_info):
        CustomUser.objects.create_superuser(**user_info)

        with pytest.raises(ValueError):
            CustomUser.objects.create_superuser(**user_info, is_admin=False)

        assert CustomUser.objects.count() == 1, "Should be created one superuser"

    # def test_unique_user(self, user_info):
    #     NotImplemented
