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

    title = models.CharField(max_length=50, null=False, blank=True)
    description = models.TextField(null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)

    level = models.CharField(max_length=50, db_index=True, choices=Level.choices)
    status = models.CharField(max_length=50, db_index=True, choices=Status.choices)

    categories = models.ManyToManyField('categories.Category')
    educations = models.ManyToManyField('educations.Education')

    assigned_to = models.ForeignKey("workers.Worker", on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'
