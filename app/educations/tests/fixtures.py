import pytest
from django.db.models import QuerySet

from educations.models import Education


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def it_education(pytech_user) -> Education:
    education, _ = Education.objects.get_or_create(name='it', user=pytech_user)
    return education


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def software_education(pytech_user) -> Education:
    software, _ = Education.objects.get_or_create(name='software', user=pytech_user)
    return software


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def network_education(pytech_user) -> Education:
    network, _ = Education.objects.get_or_create(name='network', user=pytech_user)
    return network


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def accountant_education(pytech_user) -> Education:
    accountant, _ = Education.objects.get_or_create(name='accountant', user=pytech_user)
    return accountant


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def digital_marketing_education(pytech_user) -> Education:
    digital_marketing, _ = Education.objects.get_or_create(name='digital_marketing', user=pytech_user)
    return digital_marketing


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def pytech_user_educations(pytech_user) -> QuerySet[Education]:
    objects = []
    for i in range(100):
        name = f'education_{i}'
        obj = Education(user=pytech_user, name=name)
        objects.append(obj)

    records = Education.objects.bulk_create(objects)
    return records
