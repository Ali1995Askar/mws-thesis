import pytest
from django.db.models import QuerySet

from categories.models import Category


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def python_category(pytech_user) -> Category:
    python, _ = Category.objects.get_or_create(name='python', user=pytech_user)
    return python


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def aws_category(pytech_user) -> Category:
    aws, _ = Category.objects.get_or_create(name='aws', user=pytech_user)
    return aws


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def marketing_category(pytech_user) -> Category:
    marketing, _ = Category.objects.get_or_create(name='marketing', user=pytech_user)
    return marketing


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def asp_category(pytech_user) -> Category:
    asp, _ = Category.objects.get_or_create(name='asp', user=pytech_user)
    return asp


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def java_category(pytech_user) -> Category:
    java, _ = Category.objects.get_or_create(name='java', user=pytech_user)
    return java


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def react_category(pytech_user) -> Category:
    react, _ = Category.objects.get_or_create(name='react', user=pytech_user)
    return react


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def pytech_user_categories(pytech_user) -> QuerySet[Category]:
    objects = []
    for i in range(100):
        name = f'category_{i}'
        obj = Category(user=pytech_user, name=name)
        objects.append(obj)

    records = Category.objects.bulk_create(objects)
    return records
