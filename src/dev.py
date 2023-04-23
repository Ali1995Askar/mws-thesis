from src.algorithm.max_flow.dinitz_algorithm import DinitzAlgorithm
from src.algorithm.max_flow.edmond_karp_algorithm import EdmondsKarpAlgorithm
from src.algorithm.max_flow.preflow_push_algorithm import PreFlowPushAlgorithm

if __name__ == '__main__':
    import networkx as nx

    graph = nx.DiGraph()
    graph.add_nodes_from([i for i in range(10)])

    graph.add_edges_from([(1, 6, {'capacity': 50}),
                          (1, 2, {'capacity': 5}),
                          (2, 4, {'capacity': 4}),
                          (4, 6, {'capacity': 3}), ])

    inst = EdmondsKarpAlgorithm(graph, source=1, sink=6)
    value, _ = inst.find_max_flow()
    print('EdmondsKarpAlgorithm', value)

    inst = DinitzAlgorithm(graph, source=1, sink=6)
    value, _ = inst.find_max_flow()
    print('DinitzAlgorithm', value)

    inst = PreFlowPushAlgorithm(graph, source=1, sink=6)
    value, _ = inst.find_max_flow()
    print('PreFlowPushAlgorithm', value)
