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
        return 10

    @classmethod
    def create_tasks(cls, user):
        return 10

    def handle(self, *args, **options):
        user = self.create_user_and_profile()
        print(f'Successfully created a user with the username "{user.username}" and completed the profile setup.\n')

        categories_count = self.create_categories(user)
        print(f'Successfully created {categories_count} categories records.\n')

        education_count = self.create_educations(user)
        print(f'Successfully created {education_count} education records.\n')
