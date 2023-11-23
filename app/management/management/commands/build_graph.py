from django.core.management.base import BaseCommand

from accounts.models import Profile
from educations.models import Education
from categories.models import Category
from django.contrib.auth import get_user_model
from workers.models import Worker
from tasks.models import Task
from .constants import *


class Command(BaseCommand):
    help = 'dispatch not dispatched keywords'

    def add_arguments(self, parser):
        parser.add_argument(
            '-rh_ids',
            '--route_hash_ids',
            type=str,
            nargs='+',
        )

    @classmethod
    def create_user_and_profile(cls):
        get_user_model().objects.filter(username=user_ali['username']).delete()
        user = get_user_model().objects.create_user(**user_ali)
        Profile.objects.filter(user=user).update(**profile)
        return user

    @classmethod
    def create_categories(cls, user):
        Category.objects.all().delete()
        categories_objects = []
        for category in categories:
            categories_objects.append(Category(user=user, name=category))
        Category.objects.bulk_create(categories_objects)

        return Category.objects.count()

    @classmethod
    def create_educations(cls, user):
        Education.objects.all().delete()
        educations_objects = []
        for education in educations:
            educations_objects.append(Education(user=user, name=education))
        Education.objects.bulk_create(educations_objects)

        return Education.objects.count()

    @classmethod
    def create_workers(cls, user):
        Worker.objects.all().delete()
        workers_objects = []
        for worker in workers:
            workers_objects.append(Worker(user=user, **worker))

        Worker.objects.bulk_create(workers_objects)
        return Worker.objects.count()

    @classmethod
    def create_tasks(cls, user):
        Task.objects.all().delete()
        tasks_objects = []
        for task in tasks:
            tasks_objects.append(Task(user=user, **task))

        Task.objects.bulk_create(tasks_objects)
        return Task.objects.count()

    def handle(self, *args, **options):
        user = self.create_user_and_profile()
        print(f'Successfully created a user with the username "{user.username}" and completed the profile setup.\n')

        categories_count = self.create_categories(user)
        print(f'Successfully created {categories_count} categories records.\n')

        educations_count = self.create_educations(user)
        print(f'Successfully created {educations_count} education records.\n')

        workers_count = self.create_workers(user)
        print(f'Successfully created {workers_count} workers records.\n')

        tasks_count = self.create_tasks(user)
        print(f'Successfully created {tasks_count} tasks records.\n')
