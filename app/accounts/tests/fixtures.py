import pytest
from django.test import Client
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


@pytest.fixture
@pytest.mark.django_db(transaction=True)
def authorized_client(pytech_user):
    client = Client()
    pytech_user.set_password("new_password")  # Remove quotes and set the password correctly
    pytech_user.save()  # Save the user after setting the password
    logged_in_client = client.login(username=pytech_user.username, password="new_password")  # Use the new password here
    return client


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def un_authorized_client():
    client = Client()
    return client
