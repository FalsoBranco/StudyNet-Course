import pytest
from accounts.models import CustomUser
from accounts.services import user_create
from django.core.exceptions import ValidationError

pytestmark = pytest.mark.django_db


@pytest.fixture
def user_info():
    return {
        "username": "FalsoBranco",
        "email": "falso_branco@gmail.com",
        "password": "falsopassbrancoword",
    }


class TestUserCreate:
    def test_user_creation(self, user_info):
        user_create(**user_info)
        assert CustomUser.objects.count() == 1

    def test_user_function_returning(self, user_info):
        user = user_create(**user_info)
        assert isinstance(user, CustomUser)
