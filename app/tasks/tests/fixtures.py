import pytest
from django.db.models import QuerySet

from tasks.models import Task


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def task_fix_tests(pytech_user) -> Task:
    task = Task.objects.create(
        title='Fix Tests',
        description='fix aws in bla bla bla',
        level=Task.Level.JUNIOR.value,
        status=Task.Status.OPEN.value,
        user=pytech_user
    )

    return task


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def task_deploy_service(pytech_user) -> Task:
    task = Task.objects.create(
        title='deploy_service',
        description='deploy_service bla bla bla',
        level=Task.Level.JUNIOR.value,
        status=Task.Status.OPEN.value,
        user=pytech_user

    )

    return task


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def task_connect_with_customers(pytech_user) -> Task:
    task = Task.objects.create(
        title='connect_with_customers',
        description='connect_with_customers bla bla bla',
        level=Task.Level.JUNIOR.value,
        status=Task.Status.OPEN.value,
        user=pytech_user

    )

    return task


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def task_pay_salaries(pytech_user) -> Task:
    task = Task.objects.create(
        title='pay_salaries',
        description='pay_salaries bla bla bla',
        level=Task.Level.JUNIOR.value,
        status=Task.Status.OPEN.value,
        user=pytech_user
    )
    return task


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def task_send_emails(pytech_user) -> Task:
    task = Task.objects.create(
        title='send_emails',
        description='send_emails bla bla bla',
        level=Task.Level.JUNIOR.value,
        status=Task.Status.OPEN.value,
        user=pytech_user
    )
    return task


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def task_create_new_service(pytech_user) -> Task:
    task = Task.objects.create(
        title='create_new_service',
        description='create_new_service bla bla bla',
        level=Task.Level.JUNIOR.value,
        status=Task.Status.OPEN.value,
        user=pytech_user
    )
    return task


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def task_hire_new_employee(pytech_user) -> Task:
    task = Task.objects.create(
        title='hire_new_employee',
        description='hire_new_employee bla bla bla',
        level=Task.Level.JUNIOR.value,
        status=Task.Status.OPEN.value,
        user=pytech_user
    )
    return task


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def pytech_user_tasks(pytech_user) -> QuerySet[Task]:
    objects = []
    for i in range(3000):
        title = f'task_title_{i}'
        description = f'task_description_{i}'
        obj = Task.objects.create(title=title,
                                  description=description,
                                  level=Task.Level.JUNIOR.value,
                                  status=Task.Status.OPEN.value,
                                  user=pytech_user)
        objects.append(obj)

    return Task.objects.all()
