from tasks.models import Task
from django.dispatch import receiver
from tasks.selectors import TaskSelectors
from django.db.models.signals import post_save


@receiver(post_save, sender=Task)
def add_new_task(sender, instance: Task, created, **kwargs):
    if instance.dispatch_enabled:
        connected_workers = TaskSelectors.get_connected_workers(task=instance)

        if not created:
            workers = instance.connected_workers.all()
            for worker in workers:
                worker.save()
        instance.connected_workers.set(list(connected_workers))
