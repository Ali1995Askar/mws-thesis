from networkx import DiGraph

from app.src.algorithm.max_flow.core.ford_fulkerson import ford_fulkerson


class TestFordFulkerson:
    def test_unit_1(self):
        graph = DiGraph()
        graph.add_edges_from([
            (0, 1, {'capacity': 16}),
            (0, 2, {'capacity': 13}),
            (1, 2, {'capacity': 10}),
            (1, 3, {'capacity': 12}),
            (2, 1, {'capacity': 4}),
            (2, 4, {'capacity': 14}),
            (4, 3, {'capacity': 7}),
            (3, 2, {'capacity': 9}),
            (3, 5, {'capacity': 20}),
            (4, 5, {'capacity': 4}),
        ])
        res = ford_fulkerson(graph, 0, 5)
        assert res.graph['flow_value'] == 23

    def test_unit_2(self):
        graph = DiGraph()
        graph.add_edges_from([
            (0, 1, {'capacity': 10}),
            (0, 2, {'capacity': 10}),
            (1, 2, {'capacity': 2}),
            (1, 4, {'capacity': 8}),
            (1, 3, {'capacity': 4}),
            (3, 5, {'capacity': 10}),
            (4, 5, {'capacity': 10}),
            (4, 3, {'capacity': 6}),
            (2, 4, {'capacity': 9}),

        ])
        res = ford_fulkerson(graph, 0, 5)
        assert res.graph['flow_value'] == 19

    def test_unit_3(self):
        graph = DiGraph()
        graph.add_edges_from([(0, 5, {'capacity': 0})])
        res = ford_fulkerson(graph, 0, 5)
        assert res.graph['flow_value'] == 0

    def test_unit_4(self):
        graph = DiGraph()
        graph.add_edges_from([
            (0, 1, {'capacity': 3}),
            (1, 2, {'capacity': 2}),
            (2, 3, {'capacity': 4})
        ])
        res = ford_fulkerson(graph, 0, 3)
        assert res.graph['flow_value'] == 2

    def test_unit_5(self):
        graph = DiGraph()
        graph.add_edges_from([
            (0, 1, {'capacity': 3}),
            (0, 2, {'capacity': 2}),
            (1, 3, {'capacity': 3}),
            (2, 3, {'capacity': 2})
        ])
        res = ford_fulkerson(graph, 0, 3)
        assert res.graph['flow_value'] == 5
