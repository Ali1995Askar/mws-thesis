from tasks import models
from django.contrib import admin
from django_admin_relation_links import AdminChangeLinksMixin


@admin.register(models.Task)
class TaskAdmin(AdminChangeLinksMixin, admin.ModelAdmin):
    change_links = ['user', 'assigned_to']

    list_display = [
        'user_link',
        'title',
        'level',
        'status',
        'assigned_to_link'
        'created_on_datetime'
        'updated_on_datetime'
    ]
