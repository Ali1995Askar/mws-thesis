from django.contrib import admin
from tasks import models


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'assigned_to']
