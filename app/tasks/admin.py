from tasks import models
from django.contrib import admin
from django_admin_relation_links import AdminChangeLinksMixin


@admin.register(models.Task)
class TaskAdmin(AdminChangeLinksMixin, admin.ModelAdmin):
    change_links = ['user', 'assigned_to']

    list_display = [
        'title',
        'status',
        'categories_list',

        'user_link',

    ]

    list_filter = [
        'status',
        'categories',
    ]

    search_fields = [
        'title'
    ]

    @staticmethod
    def categories_list(obj):
        to_show = ''
        for category in obj.categories.all():
            to_show += category.name + ', '
        return to_show
