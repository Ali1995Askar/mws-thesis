from tasks.models import Task
from django.db.models import Count

from workers.models import Worker


class Selectors:
    @staticmethod
    def get_tasks_count_by_status():
        status_choices = Task.Status.choices

        tasks_status_counts = Task.objects.values('status').annotate(
            status_count=Count('status'),
        ).values('status', 'status_count')

        tasks_status_counts_list = list(tasks_status_counts)
        status_dict = {task['status']: task['status_count'] for task in tasks_status_counts_list}
        for choice, _ in status_choices:
            if choice not in status_dict.keys():
                status_dict[choice] = 0

        return status_dict

    @staticmethod
    def get_workers_count_by_status():
        status_choices = Worker.Status.choices

        workers_status_counts = Worker.objects.values('status').annotate(
            status_count=Count('status'),
        ).values('status', 'status_count')

        workers_status_counts_list = list(workers_status_counts)
        status_dict = {worker['status']: worker['status_count'] for worker in workers_status_counts_list}
        for choice, _ in status_choices:
            if choice not in status_dict.keys():
                status_dict[choice] = 0

        return status_dict
