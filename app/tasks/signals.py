from tasks.models import Task
from django.dispatch import receiver
from django.db.models.signals import post_save
from tasks.services import TaskServices


@receiver(post_save, sender=Task)
def add_new_task(sender, instance: Task, created, **kwargs):
    TaskServices.add_new_task_to_bipartite_graph(task=instance, created=created)
