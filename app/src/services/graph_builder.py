from tasks.models import Task
from typing import List, Tuple
from dataclasses import dataclass
from workers.models import Worker
from django.db.models import QuerySet
from django.contrib.auth.models import User
from src.graph.bipartite_graph import BipartiteGraph


@dataclass
class Edge:
    worker_id: str
    task_id: str

    def as_tuple(self) -> Tuple[str, str]:
        return self.worker_id, self.task_id


class GraphBuilder:
    def __init__(self, user: User):
        self.user: User = user
        self.nodes: List[str] = []
        self.edges: List[Tuple[str, str]] = []

    def get_bipartite_graph(self):
        free_workers = self.get_free_workers()
        open_tasks = self.get_open_tasks()
        self.set_nodes_edges(open_tasks, free_workers)
        bipartite_graph = self.prepare_graph()
        return bipartite_graph

    def get_free_workers(self) -> List[str]:
        free_workers = Worker.objects.prefetch_related(
            'connected_tasks'
        ).filter(
            user=self.user, status=Worker.Status.FREE
        ).values_list('id', flat=True)
        free_workers = list(free_workers)
        return free_workers

    def get_open_tasks(self) -> QuerySet[Task]:
        open_tasks = Task.objects.prefetch_related('connected_workers').filter(user=self.user, status=Task.Status.OPEN)
        return open_tasks

    def set_nodes_edges(self, tasks: QuerySet[Task], free_workers: List[str]) -> None:
        edges = []

        for task in tasks:
            connected_workers = task.connected_workers.all()
            for connected_worker in connected_workers:
                if connected_worker.id not in free_workers:
                    continue

                self.nodes.append(f'worker-{connected_worker.id}')
                self.nodes.append(f'task-{task.id}')
                edge_obj = Edge(worker_id=f'worker-{connected_worker.id}', task_id=f'task-{task.id}')
                edge = edge_obj.as_tuple()
                edges.append(edge)

        self.edges = edges

    def prepare_graph(self) -> BipartiteGraph:
        inst = BipartiteGraph()
        inst.build_manually(nodes=self.nodes, edges=self.edges)
        return inst
