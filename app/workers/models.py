from django.db import models
from django.contrib.auth.models import User


class Worker(models.Model):
    class Status(models.Choices):
        FREE = 'FREE'
        OCCUPIED = 'OCCUPIED'

    class Level(models.Choices):
        JUNIOR = 'JUNIOR'
        MID = 'MID'
        SENIOR = 'SENIOR'

    # Personal Info
    first_name = models.CharField(max_length=50, null=False, blank=True)
    last_name = models.CharField(max_length=50, null=False, blank=True)
    email = models.EmailField(null=False, blank=False)

    # Career Info
    categories = models.ManyToManyField('categories.Category')
    education = models.ForeignKey('educations.Education', null=True, blank=True, on_delete=models.CASCADE)

    level = models.CharField(max_length=50, db_index=True, choices=Level.choices)
    status = models.CharField(max_length=50, db_index=True, choices=Status.choices)

    # Company Relation
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
