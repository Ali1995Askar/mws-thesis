from django.dispatch import receiver
from management.models import BipartiteGraph
from django.contrib.auth.models import User
from django.db.models.signals import post_save


@receiver(post_save, sender=User)
def add_new_task(sender, instance, created, **kwargs):
    if created:
        BipartiteGraph.objects.create(user=instance)
