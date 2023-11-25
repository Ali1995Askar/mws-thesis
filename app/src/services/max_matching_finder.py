import time
from typing import Type
from tasks.models import Task
from workers.models import Worker
from core.factories import HeuristicFactory

from django.contrib.auth.models import User
from src.graph.bipartite_graph import BipartiteGraph
from src.solvers.max_matching.max_matching_solver import MaxMatchingSolver
from src.solvers.max_matching.heuristics.abstract_heuristic import AbstractHeuristic
from management.models import ExecutionHistory, MaxMatching as MaxMatchingModel, HeuristicMatching


class MaxMatching:
    def __init__(self, user: User, graph: BipartiteGraph, heuristic_algorithm: str):
        self.user = user
        self.graph = graph
        self.heuristic_algorithm = heuristic_algorithm
        self.max_matching_solver = MaxMatchingSolver()
        self.heuristic_execution_time: float = 0
        self.max_matching_execution_time: float = 0

    def execute(self):
        heuristic_solver = self.get_heuristic_solver()
        self.solve(heuristic_solver=heuristic_solver, bipartite_graph=self.graph)
        max_matching_history = self.save_max_matching_model()
        heuristic_matching_history = self.save_heuristic_matching_model()
        self.save_execution_history(max_matching_history, heuristic_matching_history)
        self.update_nodes_status()

    def solve(self, heuristic_solver: Type[AbstractHeuristic], bipartite_graph: BipartiteGraph):
        solve_start_time = time.time()
        heuristic_start_time = time.time()
        self.max_matching_solver.set_bipartite_graph(bipartite_graph)
        self.max_matching_solver.reduce_to_max_flow()
        self.max_matching_solver.init_heuristic_algorithm(heuristic_solver)
        self.max_matching_solver.build_initial_flow()
        heuristic_end_time = time.time()
        self.heuristic_execution_time = round(heuristic_end_time - heuristic_start_time, 4)
        self.max_matching_solver.init_ford_fulkerson_solver()
        self.max_matching_solver.find_max_matching()
        solve_end_time = time.time()
        self.max_matching_execution_time = round(solve_end_time - solve_start_time, 4)

    def get_heuristic_solver(self):
        heuristic_solver: Type[AbstractHeuristic] = HeuristicFactory.get_algo_inst_by_name(self.heuristic_algorithm)
        return heuristic_solver

    def update_nodes_status(self):
        workers_ids = []
        for matching_edge in self.max_matching_solver.get_max_matching_edges():
            task_task_id: str = matching_edge[0]
            worker_worker_id: str = matching_edge[1]

            task_id = task_task_id.split('-')[1]
            workers_id = worker_worker_id.split('-')[1]
            workers_ids.append(workers_id)
            Task.objects.filter(id=task_id).update(status=Task.Status.PROGRESS, assigned_to_id=workers_id)

        Worker.objects.filter(id__in=workers_ids).update(status=Worker.Status.OCCUPIED)

    def save_max_matching_model(self):
        max_matching = MaxMatchingModel.objects.create(
            user=self.user,
            max_matching_edges=self.max_matching_solver.get_max_matching_edges(),
            execution_time=self.max_matching_execution_time,
            max_matching=self.max_matching_solver.get_matching_value(),

        )
        return max_matching

    def save_heuristic_matching_model(self):
        heuristic_matching = HeuristicMatching.objects.create(
            user=self.user,
            heuristic_matching_edges=self.max_matching_solver.get_max_matching_edges(),
            heuristic_matching=len(self.max_matching_solver.heuristic_algorithm.matching_edges),
            execution_time=self.heuristic_execution_time,
        )

        return heuristic_matching

    def save_execution_history(self, max_matching_model: MaxMatchingModel, heuristic_matching_model: HeuristicMatching):
        edges_count = len(self.graph.graph.edges)
        print(edges_count)
        edges_count = edges_count // 2

        if self.graph.red_nodes and self.graph.blue_nodes:
            red_nodes_count = len(self.graph.red_nodes)
            blue_nodes_count = len(self.graph.blue_nodes)
            graph_density = edges_count / (red_nodes_count * blue_nodes_count)
            graph_density = round(graph_density, 3)

        else:
            graph_density = 0
        execution_history = ExecutionHistory.objects.create(
            user=self.user,
            max_matching=max_matching_model,
            heuristic_matching=heuristic_matching_model,
            graph_density=graph_density,
        )

        return execution_history
