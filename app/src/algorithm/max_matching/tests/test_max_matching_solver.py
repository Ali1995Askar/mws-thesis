import random

import pytest
from app.src.graph.bipartite_graph import BipartiteGraph
from app.src.algorithm.max_flow.ford_fulkerson_solver import FordFulkersonSolver
from app.src.algorithm.max_matching.max_matching_solver import MaxMatchingSolver
from app.src.algorithm.max_flow.abstract_max_flow_solver import AbstractMaxFlowSolver
from app.src.algorithm.max_matching.heuristics.backtracking_algo import BackTrackingAlgo


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
        graph = BipartiteGraph()
        inst = MaxMatchingSolver()
        graph.build_manually(
            nodes=[1, 2, 3, 4, 5, 6],
            edges=[(1, 4), (2, 5), (3, 6), ])

        inst.set_bipartite_graph(bipartite_graph=graph)
        inst.set_solver(solver=FordFulkersonSolver)

        assert inst.temp_graph.edges(data=True) == [(1, 4, {'capacity': 1}),
                                                    (2, 5, {'capacity': 1}),
                                                    (3, 6, {'capacity': 1}),
                                                    (4, 1, {'capacity': 1}),
                                                    (5, 2, {'capacity': 1}),
                                                    (6, 3, {'capacity': 1})]

        inst.bipartite_graph.split_nodes()

        inst.direct_bipartite_graph()

        assert inst.temp_graph.edges(data=True) == [
            (1, 4, {'capacity': 1}),
            (1, 'source', {'capacity': 0}),

            (2, 5, {'capacity': 1}),
            (2, 'source', {'capacity': 0}),

            (3, 6, {'capacity': 1}),
            (3, 'source', {'capacity': 0}),

            (4, 1, {'capacity': 0}),
            (4, 'sink', {'capacity': 1}),

            (5, 2, {'capacity': 0}),
            (5, 'sink', {'capacity': 1}),

            (6, 3, {'capacity': 0}),
            (6, 'sink', {'capacity': 1}),

            ('source', 1, {'capacity': 1}),
            ('source', 2, {'capacity': 1}),
            ('source', 3, {'capacity': 1}),

            ('sink', 4, {'capacity': 0}),
            ('sink', 5, {'capacity': 0}),
            ('sink', 6, {'capacity': 0})
        ]

    def test_reduce_to_max_flow(self):
        graph = BipartiteGraph()
        inst = MaxMatchingSolver()
        graph.build_manually(
            nodes=[1, 2, 3, 4, 5, 6],
            edges=[(1, 4), (2, 5), (3, 6), ])

        inst.set_bipartite_graph(bipartite_graph=graph)
        inst.set_solver(solver=FordFulkersonSolver)
        inst.reduce_to_max_flow()

    def test_find_max_matching(self):
        graph = BipartiteGraph()
        inst = MaxMatchingSolver()
        graph.build_manually(
            nodes=[1, 2, 3, 4, 5, 6],
            edges=[(1, 4), (2, 5), (3, 6), ])

        inst.set_bipartite_graph(bipartite_graph=graph)
        inst.set_solver(solver=FordFulkersonSolver)
        inst.reduce_to_max_flow()
        inst.find_max_matching()
        print(inst.max_matching_edges)

    def test_find_max_matching_random(self):
        bipartite_graph = BipartiteGraph()

        for i in range(50):
            n = random.randrange(100, 1000, 50)
            d = random.uniform(0.001, 1)
            inst = MaxMatchingSolver()
            bipartite_graph.random_build(num_of_nodes=n, density=d)
            inst.set_bipartite_graph(bipartite_graph)
            inst.set_solver(FordFulkersonSolver)
            inst.reduce_to_max_flow()
            inst.find_max_matching()
            ex = []

            for u, v in inst.max_matching_edges:
                assert bipartite_graph.has_edge_with_positive_capacity(u, v)
                assert u not in ['source', 'sink']
                assert v not in ['source', 'sink']
                ex.append(u)
                ex.append(v)

            assert len(ex) == len(set(ex))
