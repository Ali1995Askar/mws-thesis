import pytest
import networkx as nx
from app.src.graph.bipartite_graph import BipartiteGraph


@pytest.fixture()
def ex_graph_1() -> nx.Graph:
    nodes = [i for i in range(4)]
    edges = [
        (0, 1, {'capacity': 3}),
        (0, 2, {'capacity': 2}),
        (1, 2, {'capacity': 1}),
        (1, 3, {'capacity': 4}),
        (2, 3, {'capacity': 2}),
    ]
    graph = nx.DiGraph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)
    return graph


@pytest.fixture()
def ex_graph_2():
    nodes = [i for i in range(4)]
    edges = []
    graph = nx.DiGraph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)
    return graph


@pytest.fixture()
def ex_graph_3():
    nodes = [i for i in range(4)]
    edges = [
        (0, 1, {'capacity': 1}),
        (1, 2, {'capacity': 1}),
        (2, 3, {'capacity': 1}),

    ]
    graph = nx.DiGraph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)
    return graph


@pytest.fixture()
def ex_graph_4():
    nodes = [i for i in range(4)]
    edges = [
        (0, 1, {'capacity': 1}),
        (0, 2, {'capacity': 2}),
        (1, 2, {'capacity': 1}),
        (1, 3, {'capacity': 1}),
        (2, 3, {'capacity': 2}),

    ]
    graph = nx.DiGraph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)
    return graph


@pytest.fixture()
def ex_graph_5():
    nodes = [i for i in range(4)]
    edges = [
        (0, 1, {'capacity': 3}),
        (0, 2, {'capacity': 2}),
        (1, 2, {'capacity': 1}),
        (1, 3, {'capacity': 3}),
        (2, 3, {'capacity': 2})]

    graph = nx.DiGraph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)
    return graph


@pytest.fixture()
def ex_graph_6():
    nodes = [i for i in range(4)]
    edges = [
        (0, 1, {'capacity': 3}),
        (1, 2, {'capacity': 1}),
        (2, 3, {'capacity': 2}),
        (3, 1, {'capacity': 1}),
        (3, 0, {'capacity': 2})]
    graph = nx.DiGraph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)
    return graph


@pytest.fixture()
def ex_graph_7():
    nodes = [i for i in range(4)]
    edges = [
        (0, 1, {'capacity': 2}),
        (2, 1, {'capacity': 1})]
    graph = nx.DiGraph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)
    return graph


@pytest.fixture()
def ex_graph_8():
    nodes = [i for i in range(4)]
    edges = [
        (0, 1, {'capacity': 3})
    ]
    graph = nx.DiGraph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)
    return graph


@pytest.fixture()
def ex_graph_9():
    nodes = [i for i in range(4)]
    edges = [
        (0, 1, {'capacity': 2.5}),
        (1, 2, {'capacity': 1.5}),
        (0, 2, {'capacity': 3})]

    graph = nx.DiGraph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)
    return graph


@pytest.fixture()
def ex_graph_10():
    nodes = [i for i in range(5)]
    edges = [
        (0, 2, {'capacity': 2}),
        (1, 3, {'capacity': 2}),
        (2, 4, {'capacity': 1}),
        (3, 4, {'capacity': 1}),
        (0, 1, {'capacity': 1}),
        (2, 3, {'capacity': 1})]

    graph = nx.DiGraph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)
    return graph


@pytest.fixture()
def ex_graph_11():
    graph = nx.complete_graph(10)
    for u, v in graph.edges():
        graph[u][v]['capacity'] = 1

    return graph


@pytest.fixture()
def ex_graph_12():
    nodes = [i for i in range(1000)]
    edges = [(i, i + 1, {'capacity': 1}) for i in range(999)]

    graph = nx.DiGraph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)
    return graph


@pytest.fixture()
def ex_bipartite_graph_1():
    bipartite_graph = BipartiteGraph()
    bipartite_graph.build_manually(
        nodes=[1, 2, 3, 4, 5, 6, 7],
        edges=[(1, 5), (2, 5), (2, 6), (3, 6), (4, 7)]
    )
    bipartite_graph.split_nodes()
    return bipartite_graph


@pytest.fixture()
def ex_bipartite_graph_2():
    bipartite_graph = BipartiteGraph()
    bipartite_graph.build_manually(
        nodes=[1, 2, 3, 4, 5, 6],
        edges=[(1, 4), (2, 5), (3, 6)]
    )
    bipartite_graph.split_nodes()
    return bipartite_graph


@pytest.fixture()
def ex_bipartite_graph_3():
    bipartite_graph = BipartiteGraph()
    bipartite_graph.build_manually(
        nodes=[i for i in range(0, 16)],
        edges=[
            (1, 8),
            (1, 14),
            (1, 10),
            (1, 11),
            (1, 9),
            (1, 13),
            (1, 15),
            (1, 12),

            (1, 8),
            (1, 14),
            (1, 10),
            (1, 11),
            (1, 9),
            (1, 13),
            (1, 15),
            (1, 12),

            (2, 13),
            (2, 9),
            (2, 12),
            (2, 15),
            (2, 10),
            (2, 14),
            (2, 8),
            (2, 11),

            (3, 13),
            (3, 14),
            (3, 8),
            (3, 15),
            (3, 12),
            (3, 11),
            (3, 10),
            (3, 9),

        ]
    )

    bipartite_graph.split_nodes()
    return bipartite_graph


@pytest.fixture()
def ex_bipartite_graph_4():
    pass


@pytest.fixture()
def ex_bipartite_graph_5():
    pass


@pytest.fixture()
def ex_bipartite_graph_6():
    pass


@pytest.fixture()
def ex_bipartite_graph_7():
    pass


@pytest.fixture()
def ex_bipartite_graph_8():
    pass


@pytest.fixture()
def ex_bipartite_graph_9():
    pass


@pytest.fixture()
def ex_bipartite_graph_10():
    pass


@pytest.fixture()
def ex_bipartite_graph_11():
    pass


@pytest.fixture()
def ex_bipartite_graph_12():
    pass
