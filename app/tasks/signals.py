from tasks.models import Task
from django.dispatch import receiver
from tasks.selectors import TaskSelectors
from django.db.models.signals import post_save

from workers.selectors import WorkerSelectors


@receiver(post_save, sender=Task)
def add_new_task(sender, instance: Task, created, **kwargs):
    if instance.dispatch_enabled:
        connected_workers = TaskSelectors.get_connected_workers(task=instance)

        for connected_worker in connected_workers:
            connected_tasks = WorkerSelectors.get_connected_tasks(worker=connected_worker)
            connected_worker.connected_tasks.set(list(connected_tasks))
        instance.connected_workers.set(list(connected_workers))
