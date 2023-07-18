from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")


class Profile(models.Model):
    contact_email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    logo = models.ImageField(upload_to='images/companies-logos', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, blank=True)
    about = models.CharField(max_length=500, null=False, blank=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True)

    created_on_datetime = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on_datetime = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return f'{self.name} Profile'
