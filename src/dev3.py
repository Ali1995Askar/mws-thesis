from src.algorithm.max_matching.heuristics.monte_carlo import MonteCarlo
from src.graph.bipartite_graph import BipartiteGraph
from src.algorithm.max_matching.max_matching import MaxMatching
from src.algorithm.max_flow.dinitz_algorithm import DinitzAlgorithm
from src.algorithm.max_flow.edmond_karp_algorithm import EdmondsKarpAlgorithm
from src.algorithm.max_flow.preflow_push_algorithm import PreFlowPushAlgorithm

if __name__ == '__main__':
    bipartite = BipartiteGraph()
    bipartite.random_build(1000, density=0.003)

    max_matching = MaxMatching()
    max_matching.set_bipartite_graph(bipartite_graph=bipartite)
    max_matching.reduce_to_max_flow()
    max_matching.set_initial_flow(heuristic_algorithm=MonteCarlo)

    max_matching.set_algorithm(algorithm=DinitzAlgorithm)
    max_matching.find_max_matching()
    max_matching.print_result()
    # max_matching.print_matching_edges()
