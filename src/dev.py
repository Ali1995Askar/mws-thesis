import networkx as nx
import matplotlib.pyplot as plt

if __name__ == '__main__':
    graph = nx.DiGraph()
    graph.add_nodes_from(['src', 1, 2, 3, 4, 5, 6])
    graph.add_edges_from([
        (1, 2),
        (2, 1),
        (1, 3),
        (1, 4),
        (1, 6),
        (3, 6),
        (4, 5),

    ])

    print(graph.nodes)
    print(graph.edges)
    print(graph.degree(1))
    print(list(graph.successors(1)))
    print(list(graph.neighbors(1)))
