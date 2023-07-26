from accounts import models
from django.contrib import admin
from django_admin_relation_links import AdminChangeLinksMixin


@admin.register(models.Profile)
class ProfileAdmin(AdminChangeLinksMixin, admin.ModelAdmin):
    change_links = ['user']

    list_display = [
        'contact_email',
        'address',
        'user_link',
        'name',
        'phone_number',
        'created_on_datetime',
        'updated_on_datetime',
    ]
