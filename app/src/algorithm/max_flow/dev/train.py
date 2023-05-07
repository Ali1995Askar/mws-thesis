import random
import time
import networkx as nx
from networkx.algorithms.flow import edmonds_karp

# A --- B --- C --- D --- E
#  \   /     |           /
#    F      G --- H --- I


if __name__ == '__main__':
    import networkx as nx
    import random
    import time

    # Generate a random graph with 100 nodes and 500 edges
    G = nx.gnm_random_graph(500, 20000)

    # Add random capacities to the edges
    capacities = {}
    for u, v in G.edges():
        capacities[(u, v)] = random.randint(1, 10)

    # Add a source node and a sink node to the graph
    source = -1
    sink = -2
    for u in list(G.nodes()):
        if u % 2 == 0:
            G.add_edge(source, u, capacity=random.randint(1, 10))
        else:
            G.add_edge(u, sink, capacity=random.randint(1, 10))

    # Compute the maximum flow using Dinic's algorithm
    start_time = time.time()
    max_flow_value = nx.maximum_flow(G, source, sink, flow_func=nx.algorithms.flow.dinitz)
    end_time = time.time()
    print("Dinic's algorithm runtime: ", end_time - start_time)
    print("Maximum flow value: ", max_flow_value[0])

    # Compute the maximum flow using Edmonds-Karp algorithm
    start_time = time.time()
    max_flow_value = nx.maximum_flow(G, source, sink, flow_func=nx.algorithms.flow.edmonds_karp)
    end_time = time.time()
    print("Edmonds-Karp algorithm runtime: ", end_time - start_time)
    print("Maximum flow value: ", max_flow_value[0])
