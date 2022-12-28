import pytest

from kyle_django_cookie_cutter_project.users.models import User
from kyle_django_cookie_cutter_project.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> User:
    return UserFactory()
