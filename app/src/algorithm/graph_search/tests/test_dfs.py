import pytest
from networkx import Graph
from networkx import DiGraph

from app.src.algorithm.graph_search.dfs import DFS


class TestDFS:
    @pytest.fixture()
    def dfs(self) -> DFS:
        inst = DFS()
        return inst

    @pytest.fixture()
    def graph(self) -> Graph:
        graph = DiGraph()
        return graph

    def test_add_to_list(self, dfs, graph):
        dfs.set_graph(graph=graph)
        assert dfs.data_structure == []
        dfs.add_to_list(1)
        assert dfs.data_structure == [1]
        dfs.add_to_list(2)
        assert dfs.data_structure == [1, 2]
        dfs.add_to_list(3)
        assert dfs.data_structure == [1, 2, 3]

    def test_pop_from_list(self, dfs, graph):
        dfs.set_graph(graph=graph)
        dfs.add_to_list(1)
        dfs.add_to_list(2)
        dfs.add_to_list(3)
        dfs.add_to_list(4)

        item = dfs.pop_from_list()
        assert item == 4

        item = dfs.pop_from_list()
        assert item == 3

        item = dfs.pop_from_list()
        assert item == 2

        item = dfs.pop_from_list()
        assert item == 1

    @pytest.mark.parametrize('edges,src,dist,res', [
        # ([], 0, 0, {}),
        # ([('A', 'B')], 'A', 'B', {'B': 'A'}),
        ([('A', 'B'), ('B', 'C'), ('C', 'A')], 'A', 'B', {'B': 'C', 'C': 'A'}),
    ])
    def test_traverse(self, dfs, graph, edges, src, dist, res):
        for edge in edges:
            print(edge)
            graph.add_edge(edge[0], edge[1])
            graph.add_edge(edge[1], edge[0])
        print(graph.is_directed())
        print(graph.edges)
        # graph.add_edges_from(edges)
        # dfs.set_graph(graph=graph)
        # print('DFS')
        # dfs.traverse(src, dist)

        # assert dfs.parent == res
        # print(dfs.find_path(src, dist))
        # print(dfs.parent)

    def test_find_path(self):
        pass
