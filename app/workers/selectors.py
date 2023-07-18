from management.models import BipartiteGraph, Edge


def add_new_worker_to_bipartite_graph(worker, user):
    connected_tasks = []  # TO implement
    edges = []

    for task in connected_tasks:
        edge = Edge(task=task, worker=worker)
        edges.append(edge)

    edges_records = Edge.objects.bulk_create(objs=edges)
    graph = BipartiteGraph.objects.get(user=user)
    graph.edges.add(*edges_records)
