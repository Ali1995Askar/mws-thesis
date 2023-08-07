from typing import List, Tuple
from tasks.selectors import TaskSelectors
from django.contrib.auth.models import User
from src.services.edge_model.edge_model import Edge
from src.graph.bipartite_graph import BipartiteGraph


class GraphBuilder:
    def __init__(self, user: User):
        self.user: User = user
        self.nodes: List[str] = []
        self.edges: List[Tuple[str, str]] = []

    def get_bipartite_graph(self):
        self.set_nodes_and_edges()
        bipartite_graph = self.build_graph()
        return bipartite_graph

    def build_graph(self) -> BipartiteGraph:
        inst = BipartiteGraph()
        inst.build_manually(nodes=self.nodes, edges=self.edges)
        return inst

    def set_nodes_and_edges(self) -> None:
        tasks_workers_dict = TaskSelectors.get_tasks_with_connected_workers(user=self.user)
        for task, workers_qs in tasks_workers_dict.items():
            task_node_id = f'task-{task.id}'
            for worker_id in workers_qs:
                worker_node_id = f'worker-{worker_id}'
                edge_obj = Edge(task_id=task_node_id, worker_id=worker_node_id)
                edge = edge_obj.as_tuple()
                self.nodes.append(task_node_id)
                self.nodes.append(worker_node_id)
                self.edges.append(edge)
