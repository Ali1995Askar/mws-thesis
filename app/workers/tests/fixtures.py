import pytest

from workers.models import Worker


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def worker_ali_askar(pytech_user):
    worker = Worker.objects.create(
        user=pytech_user,
        first_name='ali',
        last_name='askar',
        email='ali1995askar@gmail.com',
        level=Worker.Level.MID.value,
        status=Worker.Status.FREE.value,
    )

    return worker
