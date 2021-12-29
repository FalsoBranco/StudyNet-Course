import pytest
from accounts.models import CustomUser
from accounts.services import create_user
from django.core.exceptions import ValidationError

pytestmark = pytest.mark.django_db


@pytest.fixture
def user_info():
    return {
        "username": "FalsoBranco",
        "email": "falso_branco@gmail.com",
        "password": "falsopassbrancoword",
    }


class TestCreateUser:
    def test_user_creation(self, user_info):
        create_user(**user_info)
        assert CustomUser.objects.count() == 1

    def test_user_function_returning(self, user_info):
        user = create_user(**user_info)
        assert isinstance(user, CustomUser)
