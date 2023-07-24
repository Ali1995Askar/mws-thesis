from workers.models import Worker
from django.dispatch import receiver
from workers.selectors import WorkerSelectors
from django.db.models.signals import post_save


@receiver(post_save, sender=Worker)
def add_new_worker(sender, instance: Worker, created, **kwargs):
    if instance.dispatch_enabled:
        connected_tasks = WorkerSelectors.get_connected_tasks(worker=instance)

        if not created:
            tasks = instance.connected_tasks.all()
            for task in tasks:
                task.save()

        instance.connected_tasks.set(list(connected_tasks))
