from tasks import models
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=models.Task, dispatch_uid="add_new_tasks_to_graph")
def add_new_tasks_to_graph(sender, instance: models.Task, **kwargs):
    pass
