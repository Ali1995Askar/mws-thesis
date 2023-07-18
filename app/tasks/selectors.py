from management.models import BipartiteGraph, Edge


def add_new_task_to_bipartite_graph(task, user):
    connected_workers = []  # TO implement
    edges = []

    for worker in connected_workers:
        edge = Edge(task=task, worker=worker)
        edges.append(edge)

    edges_records = Edge.objects.bulk_create(objs=edges)
    graph = BipartiteGraph.objects.get(user=user)
    graph.edges.add(*edges_records)
