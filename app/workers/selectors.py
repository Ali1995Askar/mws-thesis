from typing import List
from tasks.models import Task
from workers.models import Worker
from django.contrib.auth.models import User
from django.db.models.functions import Concat
from django.db.models import QuerySet, Subquery, Count, CharField, Value, F, Q


class WorkerSelectors:

    @staticmethod
    def get_connected_tasks(worker: Worker) -> QuerySet[Task]:
        worker_categories = worker.categories.all().values('pk')
        connected_tasks = Task.objects.filter(
            status=Task.Status.OPEN,
            user=worker.user
        ).filter(
            Q(educations=worker.education) | Q(educations=None)
        )
        connected_tasks = connected_tasks.filter(
            Q(categories=None) | Q(categories__in=Subquery(worker_categories))
        )
        return connected_tasks

    @staticmethod
    def get_workers_count_by_status(user: User):
        status_choices = Worker.Status.choices

        workers_status_counts = Worker.objects.filter(
            user=user).values('status').annotate(status_count=Count('status')).values('status', 'status_count')

        workers_status_counts_list = list(workers_status_counts)
        status_dict = {worker['status']: worker['status_count'] for worker in workers_status_counts_list}
        for choice, _ in status_choices:
            if choice not in status_dict.keys():
                status_dict[choice] = 0

        return status_dict

    @staticmethod
    def get_free_workers_with_annotated_id(user: User) -> List[str]:
        free_workers = Worker.objects.filter(
            user=user, status=Worker.Status.FREE
        ).annotate(
            worker_id=Concat(Value('worker-'), F('id'), output_field=CharField())
        ).values_list('worker_id', flat=True)

        return list(free_workers)

    @staticmethod
    def get_worker_details(worker: Worker):
        categories = list(worker.categories.all().values_list('name', flat=True))
        assigned_task = Task.objects.filter(user=worker.user, assigned_to=worker).last()

        context = {
            'first_name': worker.first_name,
            'last_name': worker.last_name,
            'status': worker.status,
            'email': worker.email,
            'education': worker.education,
            'categories': categories,
            'assigned_task': assigned_task
        }

        return context
