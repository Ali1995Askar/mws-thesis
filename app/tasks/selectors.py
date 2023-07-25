from typing import Dict

from django.contrib.auth.models import User

from categories.models import Category
from educations.models import Education
from tasks.models import Task
from workers.models import Worker
from django.db.models import QuerySet, Subquery, Count, Prefetch, OuterRef


class TaskSelectors:

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
    def get_tasks_with_connected_workers(user: User) -> Dict[Task, QuerySet[Worker]]:
        task_categories = Task.objects.filter(user=user).annotate(
            category_pk=Subquery(Category.objects.filter(task=OuterRef('pk')).values('pk')[:1])
        ).values('category_pk')

        task_educations = Task.objects.filter(user=user).annotate(
            education_pk=Subquery(Education.objects.filter(task=OuterRef('pk')).values('pk')[:1])
        ).values('education_pk')

        tasks = Task.objects.filter(user=user)
        connected_workers_dict = {}

        for task in tasks:
            connected_workers_qs = Worker.objects.filter(user=user)

            if task_categories.filter(category_pk=task.pk).exists():
                connected_workers_qs = connected_workers_qs.filter(
                    categories__in=Subquery(task_categories.filter(category_pk=task.pk))
                ).annotate(
                    category_count=Count('categories')
                ).filter(category_count=task.categories.count())

            if task_educations.filter(education_pk=task.pk).exists():
                connected_workers_qs = connected_workers_qs.filter(
                    education__in=Subquery(task_educations.filter(education_pk=task.pk))
                )

            connected_workers_dict[task] = connected_workers_qs

        return connected_workers_dict

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
