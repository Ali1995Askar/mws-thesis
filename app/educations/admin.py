# Register your models here.
from django.contrib import admin
from educations import models


@admin.register(models.Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['name', ]
