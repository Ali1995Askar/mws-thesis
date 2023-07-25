from tasks.selectors import TaskSelectors
from workers.models import Worker
from django.dispatch import receiver
from workers.selectors import WorkerSelectors
from django.db.models.signals import post_save


@receiver(post_save, sender=Worker)
def add_new_worker(sender, instance: Worker, created, **kwargs):
    if instance.dispatch_enabled:
        connected_tasks = WorkerSelectors.get_connected_tasks(worker=instance)
        for connected_task in connected_tasks:
            connected_workers = TaskSelectors.get_connected_workers(task=connected_task)
            connected_task.connected_workers.set(list(connected_workers))

        instance.connected_tasks.set(list(connected_tasks))
