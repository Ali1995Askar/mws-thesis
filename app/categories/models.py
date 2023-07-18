from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_on_datetime = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on_datetime = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return f'{self.name}'
