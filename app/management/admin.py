# Register your models here.
from django.contrib import admin
from management import models


@admin.register(models.BipartiteGraph)
class BipartiteGraphAdmin(admin.ModelAdmin):
    list_display = ['worker', 'task', 'user', 'created_on_datetime', 'updated_on_datetime']


@admin.register(models.HeuristicMatching)
class HeuristicMatchingAdmin(admin.ModelAdmin):
    list_display = [
        'heuristic_matching',
        'heuristic_algorithm',
        'execution_time',
        'created_on_datetime',
        'updated_on_datetime'
    ]


@admin.register(models.MaxMatching)
class MaxMatchingAdmin(admin.ModelAdmin):
    list_display = [
        'max_matching',
        'execution_time',
        'created_on_datetime',
        'updated_on_datetime'
    ]


@admin.register(models.ExecutionHistory)
class ExecutionHistoryAdmin(admin.ModelAdmin):
    list_display = [
        'max_matching',
        'heuristic_matching',
        'created_on_datetime',
        'updated_on_datetime'
    ]
