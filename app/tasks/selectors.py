from tasks.models import Task
from workers.models import Worker
from management.models import Edge
from django.db.models import QuerySet, OuterRef, Subquery, Count, Exists, Q


class TaskSelectors:
    @staticmethod
    def delete_related_task_edges(task: Task) -> None:
        edges = Edge.objects.filter(user=task.user, task=task)
        edges.delete()

    @staticmethod
    def get_connected_workers(task: Task) -> QuerySet[Worker]:
        task_categories = task.categories.all().values('pk')
        task_educations = task.educations.all().values('pk')

        connected_workers = Worker.objects.filter(user=task.user)

        if task_categories.exists():
            connected_workers = connected_workers.filter(
                categories__in=Subquery(task_categories)
            ).annotate(
                category_count=Count('categories')
            ).filter(category_count=task_categories.count())

        if task_educations.exists():
            connected_workers = connected_workers.filter(education__in=task_educations)

        return connected_workers

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
