import pytest
import networkx as nx


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
