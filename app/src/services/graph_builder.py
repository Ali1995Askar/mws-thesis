import time

from django.db.models.functions import Concat

from tasks.models import Task
from typing import List, Tuple
from workers.models import Worker
from tasks.selectors import TaskSelectors
from django.contrib.auth.models import User
from src.services.edge_model.edge_model import Edge
from src.graph.bipartite_graph import BipartiteGraph
from django.db.models import QuerySet, Value, CharField, F

from workers.selectors import WorkerSelectors


class GraphBuilder:
    def __init__(self, user: User):
        self.user: User = user
        self.nodes: List[str] = []
        self.edges: List[Tuple[str, str]] = []
        self.graph_density = 0

    def get_bipartite_graph(self):
        start = time.time()
        free_workers, open_tasks = self.get_workers_and_tasks()
        end = time.time()
        print(f'get_workers_and_tasks {end - start}')

        self.nodes = free_workers + open_tasks
        start = time.time()
        self.edges = self.get_edges()
        end = time.time()
        print(f'get_edges {end - start}')

        self.graph_density = len(self.edges) / (len(free_workers) * len(open_tasks))

        start = time.time()
        bipartite_graph = self.build_graph()
        end = time.time()
        print(f'build_graph {end - start}')
        return bipartite_graph

    def get_free_workers(self) -> List[str]:
        free_workers = Worker.objects.filter(
            user=self.user, status=Worker.Status.FREE
        ).values_list('id', flat=True)
        free_workers = list(free_workers)
        return free_workers

    def get_open_tasks(self) -> QuerySet[Task]:
        open_tasks = Task.objects.filter(user=self.user, status=Task.Status.OPEN)
        return open_tasks

    def get_workers_and_tasks(self) -> Tuple[List[str], List[str]]:
        free_workers = WorkerSelectors.get_free_workers_with_annotated_id(user=self.user)
        open_tasks = TaskSelectors.get_free_tasks_with_annotated_id(user=self.user)
        return free_workers, open_tasks

    def get_edges(self) -> List[Tuple[str, str]]:
        edges = []
        start = time.time()
        tasks_workers_dict = TaskSelectors.get_tasks_with_connected_workers(user=self.user)
        end = time.time()
        print(f'get_tasks_with_connected_workers {end - start}')
        for task, workers_qs in tasks_workers_dict.items():
            task_node_id = f'task-{task.id}'
            for worker_id in workers_qs:
                worker_node_id = f'worker-{worker_id}'
                edge_obj = Edge(task_id=task_node_id, worker_id=worker_node_id)
                edge = edge_obj.as_tuple()
                edges.append(edge)
                print(edge)
        
        return edges

    def build_graph(self) -> BipartiteGraph:
        inst = BipartiteGraph()
        inst.build_manually(nodes=self.nodes, edges=self.edges)
        return inst
