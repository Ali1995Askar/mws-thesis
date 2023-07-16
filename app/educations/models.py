from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Education(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'