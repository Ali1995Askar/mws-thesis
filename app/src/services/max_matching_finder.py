import time
from tasks.models import Task
from dataclasses import dataclass
from workers.models import Worker
from typing import List, Tuple, Type
from django.db.models import QuerySet
from management.factories import Factory
from tasks.selectors import TaskSelectors
from django.contrib.auth.models import User
from src.graph.bipartite_graph import BipartiteGraph
from src.solvers.max_matching.max_matching_solver import MaxMatchingSolver
from src.solvers.max_matching.heuristics.abstract_heuristic import AbstractHeuristic
from management.models import ExecutionHistory, MaxMatching as MaxMatchingModel, HeuristicMatching


@dataclass
class Edge:
    worker_id: str
    task_id: str

    def as_tuple(self) -> Tuple[str, str]:
        return self.worker_id, self.task_id


class MaxMatching:
    def __init__(self, user: User, heuristic_algorithm: str):
        self.user = user
        self.graph = user.bipartitegraph
        self.heuristic_algorithm = heuristic_algorithm
        self.max_matching_solver = MaxMatchingSolver()

    def execute(self):
        base_start_time = time.time()
        free_workers = self.get_free_workers()
        open_tasks = self.get_open_tasks()
        edges = self.get_edges(open_tasks)
        bipartite_graph = self.prepare_graph(workers=free_workers, tasks=open_tasks, edges=edges)
        heuristic_solver = self.get_heuristic_solver()
        start_time = time.time()
        self.solve(heuristic_solver=heuristic_solver, bipartite_graph=bipartite_graph)
        end_time = time.time()
        print(f'solve took {end_time - start_time}')
        self.update_nodes_status()
        max_matching_history = self.save_max_matching_model(execution_time=0.1)
        heuristic_matching_history = self.save_heuristic_matching_model(heuristic_matching_edges=[], execution_time=0.1)
        self.save_execution_history(max_matching_history, heuristic_matching_history)
        base_end_time = time.time()
        print(f'execute took {base_end_time - base_start_time}')

    def solve(self, heuristic_solver: Type[AbstractHeuristic], bipartite_graph: BipartiteGraph):
        self.max_matching_solver.set_bipartite_graph(bipartite_graph)
        self.max_matching_solver.reduce_to_max_flow()
        # self.max_matching_solver.init_heuristic_algorithm(heuristic_solver)
        # self.max_matching_solver.build_initial_flow()
        self.max_matching_solver.init_ford_fulkerson_solver()
        self.max_matching_solver.find_max_matching()

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

    def update_nodes_status(self):
        workers_ids = []
        for matching_edge in self.max_matching_solver.get_max_matching_edges():
            worker_worker_id: str = matching_edge[0]
            task_task_id: str = matching_edge[1]
            task_id = task_task_id.split('-')[1]
            workers_id = worker_worker_id.split('-')[1]
            workers_ids.append(workers_id)
            Task.objects.filter(id=task_id).update(status=Task.Status.PROGRESS, assigned_to_id=workers_id)

        Worker.objects.filter(id__in=workers_ids).update(status=Worker.Status.OCCUPIED)

    def save_max_matching_model(self, execution_time):
        max_matching = MaxMatchingModel.objects.create(
            max_matching_edges=self.max_matching_solver.get_max_matching_edges(),
            execution_time=execution_time,
            max_matching=self.max_matching_solver.get_matching_value(),

        )
        return max_matching

    def save_heuristic_matching_model(self, heuristic_matching_edges, execution_time):
        heuristic_matching = HeuristicMatching.objects.create(
            heuristic_matching_edges=self.max_matching_solver.get_max_matching_edges(),
            heuristic_matching=len(heuristic_matching_edges),
            execution_time=execution_time,
            heuristic_algorithm=self.heuristic_algorithm.upper(),
        )

        return heuristic_matching

    def save_execution_history(self, max_matching_model: MaxMatchingModel, heuristic_matching_model: HeuristicMatching):
        execution_history = ExecutionHistory.objects.create(
            user=self.user,
            max_matching=max_matching_model,
            heuristic_matching=heuristic_matching_model,
            graph_density=0.4
        )

        return execution_history
