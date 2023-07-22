from tasks.models import Task
from tasks.selectors import TaskSelectors
from management.selectors import BipartiteGraphSelectors, EdgeSelectors


class TaskServices:

    @staticmethod
    def add_new_task_to_bipartite_graph(task: Task, created: bool):
        print('ssssssssssssssssssssssssssssssssssssssssssssssssss')
        TaskSelectors.delete_related_task_edges(task=task)
        connected_workers = TaskSelectors.get_connected_workers(task=task)
        print(connected_workers)
        edges = EdgeSelectors.build_edges_for_task(task=task, connected_workers=connected_workers)
        BipartiteGraphSelectors.bulk_edges_create(user=task.user, edges=edges)
