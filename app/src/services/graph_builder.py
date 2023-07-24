from tasks.models import Task
from dataclasses import dataclass
from workers.models import Worker
from typing import List, Tuple, Type
from django.db.models import QuerySet
from management.factories import Factory
from tasks.selectors import TaskSelectors
from django.contrib.auth.models import User
from src.graph.bipartite_graph import BipartiteGraph
from src.solvers.max_matching.heuristics.abstract_heuristic import AbstractHeuristic


@dataclass
class Edge:
    worker_id: str
    task_id: str

    def as_tuple(self) -> Tuple[str, str]:
        return self.worker_id, self.task_id


class GraphBuilder:
    def __init__(self, user: User):
        self.user = user

    def get_bipartite_graph(self):
        free_workers = self.get_free_workers()
        open_tasks = self.get_open_tasks()
        edges = self.get_edges(open_tasks)
        bipartite_graph = self.prepare_graph(workers=free_workers, tasks=open_tasks, edges=edges)
        return bipartite_graph

    def get_free_workers(self) -> List[str]:
        free_workers = Worker.objects.filter(user=self.user, status=Worker.Status.FREE).values_list('id', flat=True)
        free_workers = list(free_workers)
        return free_workers

    def get_open_tasks(self) -> QuerySet[Task]:
        open_tasks = Task.objects.filter(user=self.user, status=Task.Status.OPEN)
        return open_tasks

    @staticmethod
    def get_edges(tasks: QuerySet[Task]) -> List[Tuple[str, str]]:
        edges = []
        for task in tasks:
            connected_workers = TaskSelectors.get_connected_workers(task=task)
            for connected_worker in connected_workers:
                edge_obj = Edge(worker_id=f'worker-{connected_worker.id}', task_id=f'task-{task.id}')
                edge = edge_obj.as_tuple()
                edges.append(edge)
        return edges

    def get_heuristic_solver(self):
        heuristic_solver: Type[AbstractHeuristic] = Factory.get_algorithms(self.heuristic_algorithm)
        return heuristic_solver

    @staticmethod
    def prepare_graph(workers, tasks, edges) -> BipartiteGraph:
        tasks = tasks.values_list('id', flat=True)
        tasks = list(tasks)
        nodes = workers + tasks
        inst = BipartiteGraph()
        inst.build_manually(nodes=nodes, edges=edges)
        return inst
