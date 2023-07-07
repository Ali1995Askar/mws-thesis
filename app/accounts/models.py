from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")


class Profile(models.Model):
    contact_email = models.EmailField(blank=False)
    address = models.CharField(max_length=255, null=True)
    logo = models.ImageField(upload_to='images/', null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, blank=False)
    about = models.CharField(max_length=500, null=False, blank=False)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, null=True)
