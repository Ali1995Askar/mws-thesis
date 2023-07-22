from workers.models import Worker
from workers.selectors import WorkerSelectors
from management.selectors import BipartiteGraphSelectors, EdgeSelector


class WorkerServices:
    @staticmethod
    def add_new_worker_to_bipartite_graph(worker: Worker, created: bool):
        WorkerSelectors.delete_related_worker_edges(worker=worker)
        connected_tasks = WorkerSelectors.get_connected_tasks(worker=worker)
        edges = EdgeSelector.build_edges_for_worker(worker=worker, connected_tasks=connected_tasks)
        BipartiteGraphSelectors.bulk_add_edges(user=worker.user, edges=edges)
