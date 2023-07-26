from django.contrib import admin
from management import models
from django_admin_relation_links import AdminChangeLinksMixin


@admin.register(models.HeuristicMatching)
class HeuristicMatchingAdmin(AdminChangeLinksMixin, admin.ModelAdmin):
    change_links = ['user']

    list_display = [
        'user_link',
        'heuristic_algorithm',
        'heuristic_matching',
        'execution_time',
        'created_on_datetime',
        'updated_on_datetime'
    ]


@admin.register(models.MaxMatching)
class MaxMatchingAdmin(AdminChangeLinksMixin, admin.ModelAdmin):
    change_links = ['user']

    list_display = [
        'user_link',
        'max_matching',
        'execution_time',
        'created_on_datetime',
        'updated_on_datetime'
    ]


@admin.register(models.ExecutionHistory)
class ExecutionHistoryAdmin(AdminChangeLinksMixin, admin.ModelAdmin):
    change_links = ['user', 'max_matching', 'heuristic_matching']

    list_display = [
        'user_link',
        'max_matching_link',
        'heuristic_matching_link',
        'graph_density',
        'created_on_datetime',
        'updated_on_datetime'
    ]
