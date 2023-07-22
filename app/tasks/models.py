from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    class Status(models.Choices):
        OPEN = 'OPEN'
        DONE = 'DONE'
        PROGRESS = 'PROGRESS'

    class Level(models.Choices):
        JUNIOR = 'JUNIOR'
        MID = 'MID'
        SENIOR = 'SENIOR'

    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    deadline = models.DateField(null=False, blank=False)

    level = models.CharField(max_length=50, db_index=True, choices=Level.choices)
    status = models.CharField(max_length=50, db_index=True, choices=Status.choices)

    categories = models.ManyToManyField('categories.Category')
    educations = models.ManyToManyField('educations.Education')

    assigned_to = models.ForeignKey("workers.Worker", on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_on_datetime = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on_datetime = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return f'{self.title}'
