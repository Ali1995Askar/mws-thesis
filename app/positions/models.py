from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Position(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE)
    education = models.ForeignKey('educations.Education', on_delete=models.CASCADE)
