from django.contrib import admin
from accounts import models


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name']
