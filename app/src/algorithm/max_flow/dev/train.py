import time

from app.src.algorithm.max_matching.heuristics.my_algo import MyAlgo
from app.src.graph.bipartite_graph import BipartiteGraph
from app.src.algorithm.max_matching.max_matching import MaxMatching
from app.src.algorithm.max_flow.ford_fulkerson_algorithm import FordFulkersonAlgorithm

if __name__ == '__main__':
    nodes = [1, 2, 3, 4, 5, 6]
    edges = [
        (1, 4),
        (1, 6),
        (2, 4),
        (3, 4),
    ]
    bipartite_graph = BipartiteGraph()
    max_matching = MaxMatching()

    bipartite_graph.build_manually(nodes=nodes, edges=edges)
    bipartite_graph.split_nodes()
    max_matching.set_bipartite_graph(bipartite_graph=bipartite_graph)
    max_matching.set_algorithm(algorithm=FordFulkersonAlgorithm)
    max_matching.reduce_to_max_flow()
    # start_time = time.time()
    max_matching.find_max_matching()
    # end_time = time.time()
    # ford_fulkerson_algorithm_execution_time = end_time - start_time
    ford_fulkerson_algorithm_value = max_matching.max_matching_value
    print(ford_fulkerson_algorithm_value)

    my_algo = MyAlgo(bipartite_graph=bipartite_graph)
    # start_time = time.time()
    my_algo_result = my_algo.find_matching_edges()
    # end_time = time.time()
    # my_algo_time = end_time - start_time
    print(my_algo_result)
