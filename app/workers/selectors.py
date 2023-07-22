from tasks.models import Task
from workers.models import Worker
from management.models import Edge
from django.db.models import QuerySet, Count


class WorkerSelectors:
    @staticmethod
    def delete_related_worker_edges(worker: Worker):
        edges = Edge.objects.filter(worker=worker)
        edges.delete()

    @staticmethod
    def get_connected_tasks(worker) -> QuerySet[Task]:
        worker_categories = worker.categories.all()

        connected_tasks = Task.objects.filter(
            user=worker.user,
            categories__in=worker_categories,
            educations=worker.education
        )

        return connected_tasks

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
