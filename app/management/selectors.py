from tasks.models import Task
from django.db.models import Count

from workers.models import Worker


class Selectors:
    @staticmethod
    def get_tasks_count_by_status(user):
        status_choices = Task.Status.choices

        tasks_status_counts = Task.objects.filter(user=user).values('status').annotate(
            status_count=Count('status'),
        ).values('status', 'status_count')

        tasks_status_counts_list = list(tasks_status_counts)
        status_dict = {task['status']: task['status_count'] for task in tasks_status_counts_list}
        for choice, _ in status_choices:
            if choice not in status_dict.keys():
                status_dict[choice] = 0

        return status_dict

    @staticmethod
    def get_workers_count_by_status(user):
        status_choices = Worker.Status.choices

        workers_status_counts = Worker.objects.filter(user=user).values('status').annotate(
            status_count=Count('status'),
        ).values('status', 'status_count')

        workers_status_counts_list = list(workers_status_counts)
        status_dict = {worker['status']: worker['status_count'] for worker in workers_status_counts_list}
        for choice, _ in status_choices:
            if choice not in status_dict.keys():
                status_dict[choice] = 0

        return status_dict

    @staticmethod
    def get_latest_graph_info(user):
        return {
            'graph_density': 0.15,
            'max_degree': 55,
            'min_degree': 10,
        }

    @staticmethod
    def get_latest_execution_history(user):
        return {
            'execution_time': 0.005,
            'matching': 55,
            'used_heuristic_algorithm': "Limit Min Degree"
        }
