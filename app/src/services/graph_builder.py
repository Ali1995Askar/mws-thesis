from typing import List
from tasks.models import Task
from management.models import Edge
from django.db.models import QuerySet
from django.contrib.auth.models import User
from tasks.selectors import TaskSelectors


class GraphBuilder:
    def __init__(self, user: User):
        self.user = user
        self.graph = user.bipartitegraph

    def execute(self):
        tasks = self.get_tasks()
        edges = self.build_edges(tasks)
        edges_qs = self.bulk_create_edges(edges)
        self.set_graph_edges(edges_qs)

    def get_tasks(self) -> QuerySet[Task]:
        qs = Task.objects.filter(user=self.user, status=Task.Status.OPEN)
        return qs

    def build_edges(self, tasks: QuerySet[Task]) -> List[Edge]:
        edges = []
        for task in tasks:
            connected_workers = TaskSelectors.get_connected_workers(task=task)
            for connected_worker in connected_workers:
                edge = Edge(user=self.user, task=task, worker=connected_worker)
                edges.append(edge)
        return edges

    @staticmethod
    def bulk_create_edges(edges: List[Edge]) -> QuerySet[Edge]:
        edges_qs = Edge.objects.bulk_create(objs=edges, ignore_conflicts=True)
        return edges_qs

    def set_graph_edges(self, edges_qs) -> None:
        self.graph.edges.set(edges_qs)
