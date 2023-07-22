from typing import List

from django.db.models import QuerySet

from tasks.models import Task
from workers.models import Worker
from management.models import Edge, BipartiteGraph
from django.contrib.auth.models import User


class BipartiteGraphSelectors:
    @staticmethod
    def bulk_add_edges(user: User, edges: List[Edge]):
        edges_records = Edge.objects.bulk_create(objs=edges)
        graph = BipartiteGraph.objects.get(user=user)
        graph.edges.add(*edges_records)

    @staticmethod
    def get_latest_graph_data(user):
        return {
            'graph_density': 0.15,
            'max_degree': 55,
            'min_degree': 10,
        }


class EdgeSelector:
    @staticmethod
    def build_edges_for_task(task: Task, connected_workers: QuerySet[Worker]) -> List[Edge]:
        edges = []

        for worker in connected_workers:
            edge = Edge(task=task, worker=worker)
            edges.append(edge)

        return edges

    @staticmethod
    def build_edges_for_worker(worker: Worker, connected_tasks: QuerySet[Task]) -> List[Edge]:
        edges = []

        for task in connected_tasks:
            edge = Edge(task=task, worker=worker)
            edges.append(edge)

        return edges


class ExecutionHistorySelector:
    @staticmethod
    def get_latest_execution_history(user):
        return {
            'execution_time': 0.005,
            'matching': 55,
            'used_heuristic_algorithm': "Limit Min Degree"
        }
