import pytest
from workers.models import Worker
from django.db.models import QuerySet


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def worker_ali_askar(pytech_user) -> Worker:
    worker = Worker.objects.create(
        user=pytech_user,
        first_name='ali',
        last_name='askar',
        email='ali1995askar@gmail.com',
        level=Worker.Level.MID.value,
        status=Worker.Status.FREE.value,
    )

    return worker


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def worker_ahmad(pytech_user) -> Worker:
    worker = Worker.objects.create(
        user=pytech_user,
        first_name='ahmad',
        last_name='askar',
        email='ali1995askar@gmail.com',
        level=Worker.Level.MID.value,
        status=Worker.Status.FREE.value,
    )

    return worker


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def worker_omar(pytech_user) -> Worker:
    worker = Worker.objects.create(
        user=pytech_user,
        first_name='omar',
        last_name='askar',
        email='ali1995askar@gmail.com',
        level=Worker.Level.MID.value,
        status=Worker.Status.FREE.value,
    )

    return worker


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def worker_tommy(pytech_user) -> Worker:
    worker = Worker.objects.create(
        user=pytech_user,
        first_name='tommy',
        last_name='askar',
        email='ali1995askar@gmail.com',
        level=Worker.Level.MID.value,
        status=Worker.Status.FREE.value,
    )

    return worker


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def worker_bruno(pytech_user) -> Worker:
    worker = Worker.objects.create(
        user=pytech_user,
        first_name='bruno',
        last_name='askar',
        email='ali1995askar@gmail.com',
        level=Worker.Level.MID.value,
        status=Worker.Status.FREE.value,
    )

    return worker


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def pytech_user_workers(pytech_user) -> QuerySet[Worker]:
    for i in range(10):
        first_name = f'first_name_{i}'
        last_name = f'last_name_{i}'
        email = f'email_{i}@gmail.com'
        Worker.objects.create(user=pytech_user,
                              first_name=first_name,
                              last_name=last_name,
                              email=email,
                              level=Worker.Level.MID.value,
                              status=Worker.Status.FREE.value)

    return Worker.objects.all()
