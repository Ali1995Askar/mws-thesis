from categories import models
from django.contrib import admin
from django_admin_relation_links import AdminChangeLinksMixin


@admin.register(models.Category)
class CategoryAdmin(AdminChangeLinksMixin, admin.ModelAdmin):
    change_links = ['user']

    list_display = [
        'user_link',
        'name',
        'created_on_datetime',
        'updated_on_datetime',
    ]
