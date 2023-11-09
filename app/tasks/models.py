import datetime

from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Task(models.Model):
    class Status(models.Choices):
        OPEN = 'OPEN'
        DONE = 'DONE'
        PROGRESS = 'PROGRESS'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dispatch_enabled = settings.DISPATCH_ENABLED

    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    deadline = models.DateField(default=datetime.date.today, null=True, blank=True)

    status = models.CharField(max_length=50, db_index=True, choices=Status.choices)

    categories = models.ManyToManyField('categories.Category', blank=True)
    educations = models.ManyToManyField('educations.Education', blank=True)

    assigned_to = models.ForeignKey("workers.Worker", on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_on_datetime = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on_datetime = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return f'{self.title}'
