# Register your models here.
from django.contrib import admin
from departments import models


@admin.register(models.Department)
class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ['name']
