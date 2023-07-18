from workers import models
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=models.Worker, dispatch_uid="add_new_worker_to_graph")
def add_new_worker_to_graph(sender, instance: models.Worker, **kwargs):
    pass
