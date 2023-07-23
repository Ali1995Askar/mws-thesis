from workers.models import Worker
from django.dispatch import receiver
from workers.selectors import WorkerSelectors
from django.db.models.signals import post_save
from management.selectors import BipartiteGraphSelectors, EdgeSelectors


@receiver(post_save, sender=Worker)
def add_new_worker(sender, instance: Worker, created, **kwargs):
    if instance.dispatch_enabled:
        WorkerSelectors.delete_related_worker_edges(worker=instance)
        connected_tasks = WorkerSelectors.get_connected_tasks(worker=instance)
        edges = EdgeSelectors.build_edges_for_worker(worker=instance, connected_tasks=connected_tasks)
        BipartiteGraphSelectors.bulk_edges_create(edges=edges)
        BipartiteGraphSelectors.reset_bipartite_edges(user=instance.user)
