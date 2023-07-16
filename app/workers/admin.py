from django.contrib import admin
from workers import models


@admin.register(models.Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['first_name']
