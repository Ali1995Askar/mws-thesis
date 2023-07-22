from typing import List
from tasks.models import Task
from workers.models import Worker
from django.db.models import QuerySet, Count
from management.models import Edge, BipartiteGraph
from django.contrib.auth.models import User


class BipartiteGraphSelectors:
    @staticmethod
    def bulk_edges_create(user: User, edges: List[Edge]):
        Edge.objects.bulk_create(objs=edges, ignore_conflicts=True)
        edges = Edge.objects.filter(user=user)
        user.bipartitegraph.edges.set(edges)

    @staticmethod
    def get_latest_graph_data(user):
        workers_count = Worker.objects.all().count()
        tasks_count = Task.objects.all().count()
        edges_count = user.bipartitegraph.edges.all().count()
        worker_counts = Edge.objects.values('worker').annotate(count=Count('worker')).order_by('-count')

        max_repeated_worker = worker_counts.first()
        min_repeated_worker = worker_counts.last()

        max_repeated_worker = max_repeated_worker['count'] if max_repeated_worker else 0
        min_repeated_worker = min_repeated_worker['count'] if min_repeated_worker else 0

        try:
            graph_density = edges_count / (workers_count * tasks_count)
        except ZeroDivisionError:
            graph_density = 0

        return {
            'graph_density': graph_density,
            'max_degree': max_repeated_worker,
            'min_degree': min_repeated_worker,
        }


class EdgeSelectors:
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


class ExecutionHistorySelectors:
    @staticmethod
    def get_latest_execution_history(user):
        return {
            'execution_time': 0.005,
            'matching': 55,
            'used_heuristic_algorithm': "Limit Min Degree"
        }
