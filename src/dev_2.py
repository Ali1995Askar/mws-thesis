from src.graph.bipartite_graph import BipartiteGraph
import networkx as nx

if __name__ == '__main__':
    bipartite_graph = BipartiteGraph()
    bipartite_graph.build_manually(nodes=[i for i in range(5)],
                                   edges=[(1, 2,),
                                          (2, 1,),
                                          (3, 4),
                                          (4, 3),
                                          (1, 3),
                                          (3, 1)])
    if bipartite_graph.is_bipartite():
        r, b = bipartite_graph.split_nodes()
        print(r)
        print(b)

    else:
        print('Not Bipartite')
