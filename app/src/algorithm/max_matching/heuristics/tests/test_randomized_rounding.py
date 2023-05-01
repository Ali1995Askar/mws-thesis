from app.src.algorithm.max_matching.heuristics.randomized_rounding import RandomizedRounding


class TestRandomizedRounding:
    def test_matching_edges_ex_1(self, ex_bipartite_graph_1):
        inst = RandomizedRounding(bipartite_graph=ex_bipartite_graph_1)
        x = inst.find_matching_edges()
        print(x)

    def test_matching_edges_ex_2(self, ex_bipartite_graph_2):
        inst = RandomizedRounding(bipartite_graph=ex_bipartite_graph_2)
        x = inst.find_matching_edges()
        print(x)
