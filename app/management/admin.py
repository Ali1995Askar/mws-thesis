# Register your models here.
from django.contrib import admin
from management import models


@admin.register(models.BipartiteGraph)
class BipartiteGraphAdmin(admin.ModelAdmin):
    list_display = ['worker', 'task', 'user', 'created_on_datetime', 'updated_on_datetime']


@admin.register(models.ExecutionHistory)
class ExecutionHistoryAdmin(admin.ModelAdmin):
    list_display = ['heuristic_matching', 'heuristic_matching', 'max_matching', 'heuristic_algorithm', 'execution_time']
