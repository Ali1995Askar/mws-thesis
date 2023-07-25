from tasks.models import Task
from workers.models import Worker
from django.db.models import QuerySet, Count, Subquery, Q


class WorkerSelectors:

    @staticmethod
    def get_connected_tasks(worker: Worker) -> QuerySet[Task]:
        worker_categories = worker.categories.all().values('pk')
        connected_tasks = Task.objects.filter(Q(educations=worker.education) | Q(educations=None), user=worker.user)
        connected_tasks = connected_tasks.filter(Q(categories=None) | Q(categories__in=Subquery(worker_categories)))

        return connected_tasks

    @staticmethod
    def get_workers_count_by_status(user):
        status_choices = Worker.Status.choices

        workers_status_counts = Worker.objects.filter(
            user=user).values('status').annotate(status_count=Count('status')).values('status', 'status_count')

        workers_status_counts_list = list(workers_status_counts)
        status_dict = {worker['status']: worker['status_count'] for worker in workers_status_counts_list}
        for choice, _ in status_choices:
            if choice not in status_dict.keys():
                status_dict[choice] = 0

        return status_dict
