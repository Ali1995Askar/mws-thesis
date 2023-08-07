from django.db import models
from django.contrib.auth.models import User


class HeuristicMatching(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    heuristic_matching_edges = models.JSONField(null=True, blank=True)
    execution_time = models.FloatField(null=False, blank=False)
    heuristic_matching = models.IntegerField(null=False, blank=False)
    created_on_datetime = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on_datetime = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return f'{self.heuristic_matching} took {self.execution_time}'


class MaxMatching(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    max_matching_edges = models.JSONField(null=True, blank=True)
    execution_time = models.FloatField(null=False, blank=False)
    max_matching = models.IntegerField(null=False, blank=False)
    created_on_datetime = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on_datetime = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return f'{self.max_matching} took {self.execution_time}'


class ExecutionHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    max_matching = models.ForeignKey(MaxMatching, on_delete=models.CASCADE, null=True, blank=True)
    heuristic_matching = models.ForeignKey(HeuristicMatching, on_delete=models.CASCADE, null=True, blank=True)
    graph_density = models.FloatField(null=False, blank=False)
    created_on_datetime = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on_datetime = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return f'History heuristic: {self.heuristic_matching} -- max-matching {self.max_matching}'


class ContactUs(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    subject = models.CharField(max_length=255, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
