from tasks.models import Task
from django.dispatch import receiver
from tasks.selectors import TaskSelectors
from django.db.models.signals import post_save
from management.selectors import BipartiteGraphSelectors, EdgeSelectors


@receiver(post_save, sender=Task)
def add_new_task(sender, instance: Task, created, **kwargs):
    if instance.dispatch_enabled:
        TaskSelectors.delete_related_task_edges(task=instance)
        connected_workers = TaskSelectors.get_connected_workers(task=instance)
        edges = EdgeSelectors.build_edges_for_task(task=instance, connected_workers=connected_workers)
        BipartiteGraphSelectors.bulk_edges_create(edges=edges)
        BipartiteGraphSelectors.reset_bipartite_edges(user=instance.user)
