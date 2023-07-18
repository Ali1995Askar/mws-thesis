from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Edge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, unique=True)
    worker = models.ForeignKey('workers.Worker', on_delete=models.CASCADE, null=False, blank=False)
    task = models.ForeignKey('tasks.Task', on_delete=models.CASCADE, null=False, blank=False)
    created_on_datetime = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on_datetime = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        unique_together = ('user', 'worker', 'task')

    def __str__(self):
        return f'{self.worker} <---> {self.task}'


class BipartiteGraph(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, unique=True)
    edges = models.ManyToManyField(Edge, related_name='edges')
    created_on_datetime = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on_datetime = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return f'{self.user.username} Graph'


class HeuristicMatching(models.Model):
    class HeuristicAlgorithm(models.Choices):
        STATIC_MIN_DEGREE = 'STATIC_MIN_DEGREE'
        DYNAMIC_MIN_DEGREE = 'DYNAMIC_MIN_DEGREE'
        LIMIT_MIN_DEGREE = 'LIMIT_MIN_DEGREE'

        SIMPLE_GREEDY = 'SIMPLE_GREEDY'
        MONTE_CARLO = 'MONTE_CARLO'
        RANDOMIZED_ROUNDING = 'RANDOMIZED_ROUNDING'

        MODIFIED_GREEDY = 'MODIFIED_GREEDY'

    heuristic_matching_edges = models.JSONField()
    execution_time = models.FloatField(null=False, blank=False)
    heuristic_matching = models.IntegerField(null=False, blank=False)
    heuristic_algorithm = models.CharField(max_length=50, db_index=True, choices=HeuristicAlgorithm.choices)
    created_on_datetime = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on_datetime = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return f'{self.heuristic_matching} took {self.execution_time} by {self.heuristic_algorithm}'


class MaxMatching(models.Model):
    max_matching_edges = models.JSONField()
    execution_time = models.FloatField(null=False, blank=False)
    max_matching = models.IntegerField(null=False, blank=False)
    created_on_datetime = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on_datetime = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return f'{self.max_matching} took {self.execution_time}'


class ExecutionHistory(models.Model):
    max_matching = models.ForeignKey(MaxMatching, on_delete=models.CASCADE, null=False, blank=False)
    heuristic_matching = models.ForeignKey(HeuristicMatching, on_delete=models.CASCADE, null=False, blank=False)

    created_on_datetime = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on_datetime = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return f'History heuristic: {self.heuristic_matching} -- max-matching {self.max_matching}'
