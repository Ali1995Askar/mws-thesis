from src.algorithm.max_matching.heuristics.monte_carlo import MonteCarlo
from src.graph.bipartite_graph import BipartiteGraph
from src.algorithm.max_matching.max_matching import MaxMatching
from src.algorithm.max_flow.dinitz_algorithm import DinitzAlgorithm
from src.algorithm.max_flow.edmond_karp_algorithm import EdmondsKarpAlgorithm
from src.algorithm.max_flow.preflow_push_algorithm import PreFlowPushAlgorithm

if __name__ == '__main__':
    bipartite = BipartiteGraph()
    # bipartite.random_build(100, density=0.3)
    nodes = [node for node in range(12)]
    edges = [
        (0, 6),
        (0, 8),
        (0, 11),  #
        (1, 7),  #
        (2, 8),  #
        (3, 6),  #
        (3, 7),
        (3, 11),
        (4, 9),  #
        (5, 10),  #
        (5, 11),
    ]

    un_direct_edges = bipartite.build_un_directed_edges(edges=edges)

    bipartite.build_manually(nodes=nodes, edges=un_direct_edges)

    max_matching = MaxMatching()
    max_matching.set_bipartite_graph(bipartite_graph=bipartite)
    max_matching.reduce_to_max_flow()
    max_matching.set_initial_flow(heuristic_algorithm=MonteCarlo)

    max_matching.set_algorithm(algorithm=DinitzAlgorithm)
    max_matching.find_max_matching()
    max_matching.print_result()
    max_matching.print_matching_edges()
