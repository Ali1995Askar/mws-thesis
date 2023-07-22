import pytest
from django.contrib.auth.models import User


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def pytech_user():
    user, _ = User.objects.get_or_create(username='pytech',
                                         is_staff=True,
                                         is_superuser=True,
                                         email='ali1995askar@gmail.com')
    return user


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def svu_user():
    user, _ = User.objects.get_or_create(username='svu',
                                         is_staff=True,
                                         is_superuser=True,
                                         email='svu@gmail.com')
    return user
