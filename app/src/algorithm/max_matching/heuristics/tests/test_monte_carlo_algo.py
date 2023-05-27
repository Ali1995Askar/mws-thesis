import random
from app.src.graph.bipartite_graph import BipartiteGraph
from app.src.algorithm.max_matching.heuristics.monte_carlo_algo import MonteCarloAlgo


class TestMonteCarloAlgo:
    def test_matching_edges_ex_3(self):
        bipartite_graph = BipartiteGraph()
        bipartite_graph.random_build(num_of_nodes=10, density=1)

        inst = MonteCarloAlgo(bipartite_graph=bipartite_graph)
        matching = inst.find_matching_edges()
        ex = []
        # print(matching)
        for u, v in matching:
            ex.append(u)
            ex.append(v)

            assert bipartite_graph.graph.has_edge(u, v)
        assert len(ex) == len(set(ex))

    def test_matching_edges_ex_1(self, ex_bipartite_graph_1):
        inst = MonteCarloAlgo(bipartite_graph=ex_bipartite_graph_1)
        matching = inst.find_matching_edges()
        ex = []
        for u, v in matching:
            ex.append(u)
            ex.append(v)
            assert ex_bipartite_graph_1.graph.has_edge(u, v)
        assert len(ex) == len(set(ex))

    def test_matching_edges_ex_2(self, ex_bipartite_graph_2):
        inst = MonteCarloAlgo(bipartite_graph=ex_bipartite_graph_2)
        matching = inst.find_matching_edges()
        ex = []
        for u, v in matching:
            ex.append(u)
            ex.append(v)
            assert ex_bipartite_graph_2.graph.has_edge(u, v)
        assert len(ex) == len(set(ex))

    def test_random(self):
        bipartite_graph = BipartiteGraph()

        for i in range(100):
            n = random.randrange(100, 1000, 50)
            d = random.uniform(0.001, 1)

            bipartite_graph.random_build(num_of_nodes=n, density=d)

            inst = MonteCarloAlgo(bipartite_graph=bipartite_graph)
            matching = inst.find_matching_edges()
            ex = []

            for u, v in matching:
                assert bipartite_graph.has_edge_with_positive_capacity(u, v)
                ex.append(u)
                ex.append(v)
                assert u not in ['source', 'sink']
                assert v not in ['source', 'sink']

            assert len(ex) == len(set(ex))
