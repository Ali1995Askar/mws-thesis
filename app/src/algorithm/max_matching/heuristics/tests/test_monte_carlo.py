import random

from app.src.algorithm.max_matching.heuristics.monte_carlo import MonteCarlo
from app.src.graph.bipartite_graph import BipartiteGraph


class TestMonteCarlo:
    def test_matching_edges_ex_1(self, ex_bipartite_graph_1):
        inst = MonteCarlo(bipartite_graph=ex_bipartite_graph_1)
        matching = inst.find_matching_edges()
        ex = []
        for u, v in matching:
            ex.append(u)
            ex.append(v)
            assert ex_bipartite_graph_1.graph.has_edge(u, v)
        assert len(ex) == len(set(ex))

    def test_matching_edges_ex_2(self, ex_bipartite_graph_2):
        inst = MonteCarlo(bipartite_graph=ex_bipartite_graph_2)
        matching = inst.find_matching_edges()
        ex = []
        for u, v in matching:
            ex.append(u)
            ex.append(v)
            assert ex_bipartite_graph_2.graph.has_edge(u, v)
        assert len(ex) == len(set(ex))

    def test_random(self):
        bipartite_graph = BipartiteGraph()

        for i in range(50):
            n = random.randrange(100, 1000, 100)
            d = random.uniform(0.001, 1)
            bipartite_graph.random_build(num_of_nodes=n, density=d)
            bipartite_graph.split_nodes()
            inst = MonteCarlo(bipartite_graph=bipartite_graph)
            matching = inst.find_matching_edges()
            ex = []
            for u, v in matching:
                ex.append(u)
                ex.append(v)
                assert bipartite_graph.graph.has_edge(u, v)
            assert len(ex) == len(set(ex))
