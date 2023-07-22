from tasks.models import Task
from workers.models import Worker
from management.models import Edge
from django.db.models import QuerySet, OuterRef, Subquery, Count, Exists, Q


class TaskSelectors:
    @staticmethod
    def delete_related_task_edges(task: Task) -> None:
        edges = Edge.objects.filter(user=task.user, task=task)
        edges.delete()

    # @staticmethod
    # def get_connected_workers(task: Task) -> QuerySet[Worker]:
    #     task_categories = task.categories.all().values('pk')
    #     task_educations = task.educations.all().values('pk')
    #     worker_has_all_categories = Worker.objects.filter(
    #         user=OuterRef('user'),
    #         categories__in=Subquery(task_categories),
    #         education__in=task_educations
    #     ).annotate(
    #         category_count=Count('categories')
    #     ).values('category_count').filter(category_count=task_categories.count())
    #
    #     connected_workers = Worker.objects.filter(
    #         user=task.user,
    #         categories__in=task.categories.all(),
    #     ).annotate(
    #         has_all_categories=Exists(worker_has_all_categories),
    #     ).filter(has_all_categories=True)
    #
    #     return connected_workers

    @staticmethod
    def get_connected_workers(task: Task) -> QuerySet[Worker]:
        # Retrieve all workers that have all task categories
        worker_has_all_categories = Worker.objects.filter(
            user=OuterRef('user'),
            categories__in=task.categories.all(),
        ).annotate(category_count=Count('categories')).filter(category_count=task.categories.count())

        # Retrieve all workers that have at least one of the task educations
        worker_has_any_education = Worker.objects.filter(
            user=OuterRef('user'),
            education__in=task.educations.all(),
        ).annotate(education_count=Count('education')).filter(education_count__gt=0)

        # Retrieve all workers that have all task categories and at least one task education
        connected_workers = Worker.objects.filter(
            Q(user=task.user) | Q(user__isnull=True),  # Handle case when task.user is None (if needed)
            categories__in=task.categories.all(),
        ).annotate(
            has_all_categories=Exists(worker_has_all_categories),
            has_any_education=Exists(worker_has_any_education),
        ).filter(
            Q(has_all_categories=True) & (
                    Q(has_any_education=True) | Q(has_any_education=False, education__isnull=True))
        )

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
