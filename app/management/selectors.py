import json
import math
import random
from tasks.models import Task
from workers.models import Worker
from categories.models import Category
from educations.models import Education
from django.contrib.auth.models import User
from django.db.models import Count, F, Value, CharField, Q
from django.db.models.functions import Concat, Coalesce
from management.models import ExecutionHistory


class ManagementSelectors:

    @staticmethod
    def get_last_10_execution_history_statistics(user):
        execution_histories = ExecutionHistory.objects.filter(user=user).order_by('-created_on_datetime')[:10]
        if not execution_histories:
            return {}

        data = []
        accuracy_data = []
        execution_time_data = []
        for obj in execution_histories:
            heuristic_execution_time = obj.heuristic_matching.execution_time
            max_matching_execution_time = obj.max_matching.execution_time

            heuristic_matching = obj.heuristic_matching.heuristic_matching
            max_matching = obj.max_matching.max_matching

            graph_density = obj.graph_density
            row = {
                'graph_density': graph_density,
                'heuristic_matching': heuristic_matching,
                'heuristic_execution_time': heuristic_execution_time,
                'max_matching': max_matching,
                'max_matching_execution_time': max_matching_execution_time,
            }
            data.append(row)

            accuracy_dict = {
                'heuristic_matching': heuristic_matching,
                'max_matching': max_matching,
                'graph_density': graph_density
            }
            time_dict = {
                'heuristic_matching': heuristic_execution_time,
                'max_matching': max_matching_execution_time,
                'graph_density': graph_density
            }

            accuracy_data.append(accuracy_dict)
            execution_time_data.append(time_dict)
        context = {
            'rows': data,
            'accuracy_dict': json.dumps(accuracy_data),
            'time_dict': json.dumps(execution_time_data),

        }
        return context

    @staticmethod
    def get_last_matching_result(user):
        task_full_name = Concat(F("title"), Value(' ('), F("task_id"), Value(')'), output_field=CharField())
        worker_full_name = Concat('assigned_to__first_name', Value(' '), 'assigned_to__last_name',
                                  Value(' ('),
                                  'worker_id',
                                  Value(')'),
                                  output_field=CharField())

        rows = Task.objects.filter(user=user, assigned_to__isnull=False).annotate(worker_id=F('assigned_to_id'),
                                                                                  worker_full_name=worker_full_name,
                                                                                  task_id=F('id'),
                                                                                  task_full_name=task_full_name)

        rows = list(rows.values_list('worker_full_name', 'worker_id', 'task_id', 'task_full_name'))
        return {'rows': rows}

    @staticmethod
    def get_workers_count(user):
        workers_count = Worker.objects.filter(user=user).count()
        return workers_count

    @staticmethod
    def get_tasks_count(user):
        tasks_count = Task.objects.filter(user=user).count()
        return tasks_count

    @staticmethod
    def get_categories_count(user):
        categories_count = Category.objects.filter(user=user).count()
        return categories_count

    @staticmethod
    def get_educations_count(user):
        educations_count = Education.objects.filter(user=user).count()
        return educations_count

    @staticmethod
    def get_tasks_per_category(user):
        top_tasks = Category.objects.filter(user=user).annotate(
            num_tasks=Count('task')
        ).filter(
            num_tasks__gt=0
        ).order_by('-num_tasks').values('name', 'num_tasks')[:5]

        return list(top_tasks)

    @staticmethod
    def get_workers_per_category(user):
        top_workers = Category.objects.filter(user=user).annotate(
            num_workers=Count('worker')
        ).filter(
            num_workers__gt=0
        ).order_by('-num_workers').values('name', 'num_workers')[:5]
        return list(top_workers)

    @staticmethod
    def get_top_workers(user):
        top_workers = Worker.objects.filter(
            user=user
        ).annotate(
            categories_count=Count('categories'),
            full_name=Concat(F('first_name'), Value(' '), F('last_name')),
            education_name=Coalesce(F('education__name'), Value('-'))
        ).filter(categories_count__gt=0).order_by('categories_count')[:5]

        return list(top_workers)

    @staticmethod
    def get_top_categories(user):
        top_categories = Category.objects.filter(
            user=user,
        ).annotate(
            tasks_count=Count('task', distinct=True),
            workers_count=Count('worker', distinct=True),
        ).filter(Q(tasks_count__gt=0) | Q(workers_count__gt=0)).order_by(
            '-tasks_count'
        ).values('name', 'tasks_count', 'workers_count')[:10]
        return list(top_categories)
