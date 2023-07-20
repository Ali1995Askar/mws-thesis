# Register your models here.
from django.contrib import admin
from management import models


@admin.register(models.Edge)
class EdgeAdmin(admin.ModelAdmin):
    list_display = ['user', 'worker', 'task']


@admin.register(models.BipartiteGraph)
class BipartiteGraphAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_on_datetime', 'updated_on_datetime']


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
        'graph_density',
        'created_on_datetime',
        'updated_on_datetime'
    ]
