from tasks.models import Task
from tasks.selectors import TaskSelectors
from management.selectors import BipartiteGraphSelectors, EdgeSelector


class TaskServices:

    @staticmethod
    def add_new_task_to_bipartite_graph(task: Task, created: bool):
        TaskSelectors.delete_related_task_edges(task=task)
        connected_workers = TaskSelectors.get_connected_workers(task=task)
        edges = EdgeSelector.build_edges_for_task(task=task, connected_workers=connected_workers)
        BipartiteGraphSelectors.bulk_add_edges(user=task.user, edges=edges)
