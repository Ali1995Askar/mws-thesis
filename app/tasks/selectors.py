from tasks.models import Task
from workers.models import Worker
from management.models import Edge
from django.db.models import QuerySet, OuterRef, Subquery, Count, Exists, Q, Prefetch


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
    def get_connected_workers_for_all_tasks() -> dict:
        # Fetch all tasks and their connected workers using prefetch_related and annotations
        tasks = Task.objects.all().prefetch_related(
            Prefetch(
                'user__worker_set',
                queryset=Worker.objects.annotate(
                    category_count=Count('categories')
                ),
                to_attr='connected_workers'
            )
        )

        # Build a dictionary to store the results {'task': [connected_workers]}
        result = {}
        for task in tasks:
            result[task] = task.connected_workers

        return result

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
    def update_progress_tasks_to_open(user) -> None:
        tasks_in_progress = Task.objects.filter(user=user, status=Task.Status.PROGRESS)
        tasks_in_progress.update(assigned_to=None, status=Task.Status.OPEN)
        Worker.objects.filter(user=user).update(status=Worker.Status.FREE)

    @staticmethod
    def update_progress_tasks_to_done(user) -> None:
        tasks_in_progress = Task.objects.filter(user=user, status=Task.Status.PROGRESS)
        tasks_in_progress.update(status=Task.Status.DONE)
        Worker.objects.filter(user=user).update(status=Worker.Status.FREE)
