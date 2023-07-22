from workers.models import Worker
from django.dispatch import receiver
from workers.services import WorkerServices
from django.db.models.signals import post_save


@receiver(post_save, sender=Worker)
def add_new_worker(sender, instance: Worker, created, **kwargs):
    WorkerServices.add_new_worker_to_bipartite_graph(worker=instance, created=created)
