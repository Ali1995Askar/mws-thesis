from app.src_2.graph.graph import Graph


class TestGraph:
    def test_add_edge(self):
        inst = Graph()
        inst.add_edge(1, 3)
        assert inst.edges() == [(1, 3)]
        inst.add_edge(2, 3, 5)
        assert inst.edges() == [(1, 3), (2, 3)]
        assert inst.edges(data=True) == [(1, 3, {'capacity': 1}), (2, 3, {'capacity': 5})]

    def test_edges(self):
        inst = Graph()
        assert inst.edges() == []

    def test_nodes(self):
        inst = Graph()
        assert inst.nodes() == []

    def test_has_edge_with_positive_capacity(self):
        inst = Graph()
        inst.add_edge(1, 3, 5)
        assert inst.graph.has_edge(1, 3) is True
        inst.add_edge(2, 4, 0)
        assert inst.graph.has_edge(1, 3) is True
        assert inst.has_edge_with_positive_capacity(1, 3) is True
        assert inst.has_edge_with_positive_capacity(2, 4) is False

    def test_remove_edge(self):
        inst = Graph()

        inst.add_edge(1, 3, 5)
        inst.add_edge(2, 4, 0)

        assert len(inst.edges()) == 2

        inst.remove_edge(1, 3)
        inst.remove_edge(2, 4)

        assert len(inst.edges()) == 0

    def test_add_edges(self):
        inst = Graph()
        assert len(inst.edges()) == 0
        inst.add_edge(1, 3, 5)
        inst.add_edge(2, 4, 0)
        assert len(inst.edges()) == 2

        assert inst.edges() == [(1, 3), (2, 4)]

    def test_add_nodes(self):
        inst = Graph()
        assert len(inst.nodes()) == 0
        inst.add_nodes([1, 2, 3, 4, 5, 6])
        assert len(inst.nodes()) == 6
        assert inst.nodes() == [1, 2, 3, 4, 5, 6]

    def test_build_manually(self):
        inst = Graph()
        assert len(inst.nodes()) == 0
        assert len(inst.edges()) == 0
        inst.build_manually(
            nodes=[1, 2, 3, 4],
            edges=[
                (1, 3),
                (2, 4),
            ]
        )

        assert len(inst.nodes()) == 4
        assert len(inst.edges()) == 2
        assert inst.nodes() == [1, 2, 3, 4]
        assert inst.edges() == [(1, 3), (2, 4)]
