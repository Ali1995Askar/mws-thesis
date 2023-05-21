from app.src_2.graph.bipartite_graph import BipartiteGraph


class TestBipartiteGraph:
    def test_is_bipartite(self):
        inst = BipartiteGraph()
        assert inst.is_bipartite() is True
        inst.build_manually(
            nodes=[1, 2, 4],
            edges=[
                (1, 2),
                (2, 4),
                (4, 1)
            ]
        )
        assert inst.is_bipartite() is False

        inst.build_manually(
            nodes=[1, 2, 3, 4, 5],
            edges=[
                (1, 4),
                (2, 5),
                (1, 3)
            ]
        )

        assert inst.is_bipartite() is True

    def test_split_nodes(self):
        inst = BipartiteGraph()
        inst.build_manually(nodes=[1, 2, 3, 4, 5], edges=[(1, 4), (2, 5), (1, 3)])
        inst.is_bipartite()
        inst.split_nodes()
        assert inst.red_nodes == [1, 2]
        assert inst.blue_nodes == [4, 3, 5]

        inst = BipartiteGraph()
        inst.build_manually(nodes=[1, 2, 3, 4, 5, 6, 7], edges=[
            (1, 4),
            (1, 5),
            (1, 6),
            (2, 7),
            (3, 5)
        ])
        inst.is_bipartite()
        inst.split_nodes()
        assert set(inst.red_nodes) == {1, 2, 3}
        assert set(inst.blue_nodes) == {4, 5, 6, 7}

    def test_random_build(self):
        inst = BipartiteGraph()
        inst.random_build(num_of_nodes=6, density=0.5)
        assert len(inst.nodes()) == 6
        assert len(inst.edges()) == 5 * 2
        assert inst.is_bipartite() is True

        inst = BipartiteGraph()
        inst.random_build(num_of_nodes=6, density=1)
        assert len(inst.nodes()) == 6
        assert len(inst.edges()) == 9 * 2
        assert inst.is_bipartite() is True

        inst = BipartiteGraph()
        inst.random_build(num_of_nodes=6, density=0.1)
        assert len(inst.nodes()) == 6
        assert len(inst.edges()) == 2
        assert inst.is_bipartite() is True

        for i in range(100):
            inst.random_build(num_of_nodes=i * 5, density=i // 75)
            assert inst.is_bipartite()
