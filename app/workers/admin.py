from workers import models
from django.contrib import admin
from django_admin_relation_links import AdminChangeLinksMixin


@admin.register(models.Worker)
class WorkerAdmin(AdminChangeLinksMixin, admin.ModelAdmin):
    change_links = ['user', ]

    list_display = [
        'full_name',
        'status',

        'education',
        'categories_list',
        'user_link'

    ]
    list_filter = [
        'status',
        'categories',
    ]

    search_fields = [
        'first_name',
        'last_name'
    ]

    @staticmethod
    def full_name(obj):
        return obj.first_name + ' ' + obj.last_name

    @staticmethod
    def categories_list(obj):
        to_show = ''
        for category in obj.categories.all():
            to_show += category.name + ', \n'
        return to_show
