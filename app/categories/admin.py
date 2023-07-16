# Register your models here.
from django.contrib import admin
from categories import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'department']
