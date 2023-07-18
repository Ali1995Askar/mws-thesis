from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class BipartiteGraph(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    worker = models.ForeignKey('workers.Worker', on_delete=models.CASCADE, null=False, blank=False)
    task = models.ForeignKey('tasks.Task', on_delete=models.CASCADE, null=False, blank=False)
    created_on_datetime = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on_datetime = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        unique_together = ('worker', 'task')


class ExecutionHistory(models.Model):
    class HeuristicAlgorithm(models.Choices):
        STATIC_MIN_DEGREE = 'STATIC_MIN_DEGREE'
        DYNAMIC_MIN_DEGREE = 'DYNAMIC_MIN_DEGREE'
        LIMIT_MIN_DEGREE = 'LIMIT_MIN_DEGREE'

        SIMPLE_GREEDY = 'SIMPLE_GREEDY'
        MONTE_CARLO = 'MONTE_CARLO'
        RANDOMIZED_ROUNDING = 'RANDOMIZED_ROUNDING'

        MODIFIED_GREEDY = 'MODIFIED_GREEDY'

    execution_time = models.FloatField(null=False, blank=False)
    heuristic_matching = models.IntegerField(null=False, blank=False)
    max_matching = models.IntegerField(null=False, blank=False)
    heuristic_algorithm = models.CharField(max_length=50, db_index=True, choices=HeuristicAlgorithm.choices)
    created_on_datetime = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on_datetime = models.DateTimeField(auto_now=True, db_index=True)
