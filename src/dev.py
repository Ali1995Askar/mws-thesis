import networkx as nx

from src.algorithm.graph_traversal.bfs import BFS
from src.algorithm.graph_traversal.dfs import DFS

if __name__ == '__main__':
    G = nx.Graph()
    G.add_edges_from([(0, 1), (0, 2), (1, 3), (3, 4), (1, 4)])

    bfs = DFS(G)
    path = bfs.traverse(0, 4)
    print("DFS traversal:", bfs.visited)
    print("DFS path:", path)

    bfs = BFS(G)
    path = bfs.traverse(0, 4)
    print("BFS traversal:", bfs.visited)
    print("BFS path:", path)
