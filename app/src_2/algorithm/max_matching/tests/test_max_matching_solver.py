import pytest

from app.src_2.algorithm.max_flow.abstract_max_flow_solver import AbstractMaxFlowSolver
from app.src_2.algorithm.max_flow.ford_fulkerson_solver import FordFulkersonSolver
from app.src_2.algorithm.max_matching.heuristics.backtracking_algo import BackTrackingAlgo
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
        graph = BipartiteGraph()
        inst = MaxMatchingSolver()

        assert inst.solver is None
        inst.set_bipartite_graph(bipartite_graph=graph)
        inst.set_solver(solver=FordFulkersonSolver)
        inst.reduce_to_max_flow()
        inst.set_initial_flow(heuristic_algorithm=BackTrackingAlgo)
        assert {*list(inst.temp_graph.graph.nodes)} == {'source', 'sink'}
        assert len({*list(inst.temp_graph.graph.edges)}) == 0

    def test_add_source(self):
        graph = BipartiteGraph()
        inst = MaxMatchingSolver()

        inst.set_bipartite_graph(bipartite_graph=graph)
        assert inst.bipartite_graph.graph.has_node('source') is False
        assert inst.temp_graph.graph.has_node('source') is False
        inst.set_solver(solver=FordFulkersonSolver)
        inst.add_source()
        assert inst.bipartite_graph.graph.has_node('source') is False
        assert inst.temp_graph.graph.has_node('source') is True

        for u, v in inst.temp_graph.graph.edges:
            assert u != 'source'
            assert v != 'source'

    def test_add_sink(self):
        graph = BipartiteGraph()
        inst = MaxMatchingSolver()
        inst.set_bipartite_graph(bipartite_graph=graph)

        assert inst.bipartite_graph.graph.has_node('sink') is False
        assert inst.temp_graph.graph.has_node('sink') is False
        inst.set_solver(solver=FordFulkersonSolver)
        inst.add_sink()
        assert inst.bipartite_graph.graph.has_node('sink') is False
        assert inst.temp_graph.graph.has_node('sink') is True

        for u, v in inst.temp_graph.graph.edges:
            assert u != 'sink'
            assert v != 'sink'

    def test_direct_bipartite_graph(self):
        pass

    def test_reduce_to_max_flow(self):
        pass

    def test_find_max_matching(self):
        pass
