from workers import models
from django.contrib import admin
from django_admin_relation_links import AdminChangeLinksMixin


@admin.register(models.Worker)
class WorkerAdmin(AdminChangeLinksMixin, admin.ModelAdmin):
    change_links = ['user', ]

    list_display = [
        'first_name',
        'last_name',
        'email',
        'status',
        'user_link',
        'created_on_datetime',
        'updated_on_datetime'
    ]
