import pytest

from app.src_2.algorithm.max_flow.abstract_max_flow_solver import AbstractMaxFlowSolver
from app.src_2.algorithm.max_flow.ford_fulkerson_solver import FordFulkersonSolver
from app.src_2.graph.bipartite_graph import BipartiteGraph
from app.src_2.algorithm.max_matching.max_matching_solver import MaxMatchingSolver


class TestMaxMatchingSolver:
    def test_set_bipartite_graph(self):
        graph = BipartiteGraph()
        inst = MaxMatchingSolver()
        assert inst.bipartite_graph is None
        assert inst.temp_graph is None
        inst.set_bipartite_graph(bipartite_graph=graph)
        assert inst.bipartite_graph is graph
        assert inst.temp_graph is not None

    def test_set_algorithm(self):
        graph = BipartiteGraph()
        inst = MaxMatchingSolver()

        assert inst.solver is None
        inst.set_bipartite_graph(bipartite_graph=graph)
        inst.set_solver(solver=FordFulkersonSolver)

        assert isinstance(inst.solver, AbstractMaxFlowSolver)

    def test_set_initial_flow(self):
        pass

    def test_add_source(self):
        pass

    def test_add_sink(self):
        pass

    def test_direct_bipartite_graph(self):
        pass

    def test_reduce_to_max_flow(self):
        pass

    def test_find_max_matching(self):
        pass
