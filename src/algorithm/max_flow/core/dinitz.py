"""
Dinitz' algorithm for maximum flow problems.
"""
from collections import deque

import networkx as nx
from networkx.algorithms.flow.utils import build_residual_network
from networkx.utils import pairwise

__all__ = ["dinitz"]


def dinitz(G, s, t, capacity="capacity", residual=None, value_only=False, cutoff=None):
    R = dinitz_impl(G, s, t, capacity, residual, cutoff)
    R.graph["algorithm"] = "dinitz"
    return R


def dinitz_impl(G, s, t, capacity, residual, cutoff):
    if s not in G:
        raise nx.NetworkXError(f"node {str(s)} not in graph")
    if t not in G:
        raise nx.NetworkXError(f"node {str(t)} not in graph")
    if s == t:
        raise nx.NetworkXError("source and sink are the same node")

    if residual is None:
        R = build_residual_network(G, capacity)
    else:
        R = residual

    for u in R:

        for e in R[u].values():
            if not e.get('flow'):
                e["flow"] = 0

    # Use an arbitrary high value as infinite. It is computed
    # when building the residual network.
    INF = R.graph["inf"]

    if cutoff is None:
        cutoff = INF

    R_succ = R.succ
    R_pred = R.pred

    def breath_first_search():
        parents = {}
        queue = deque([s])
        while queue:
            if t in parents:
                break
            u = queue.popleft()
            for v in R_succ[u]:
                attr = R_succ[u][v]
                if v not in parents and attr["capacity"] - attr["flow"] > 0:
                    parents[v] = u
                    queue.append(v)
        return parents

    def depth_first_search(parents):
        print('--------Find Augmenting Path run--------')
        """Build a path using DFS starting from the sink"""
        path = []
        u = t
        flow = INF
        while u != s:
            path.append(u)
            v = parents[u]
            flow = min(flow, R_pred[u][v]["capacity"] - R_pred[u][v]["flow"])
            u = v
        path.append(s)

        # Augment the flow along the path found
        if flow > 0:
            for u, v in pairwise(path):
                R_pred[u][v]["flow"] += flow
                R_pred[v][u]["flow"] -= flow
                # print(u, '----->', v, ':', R_pred[u][v]["flow"], '--', R_pred[v][u]["flow"])
        return flow

    flow_value = 0
    while flow_value < cutoff:
        parents = breath_first_search()
        if t not in parents:
            break
        this_flow = depth_first_search(parents)
        if this_flow * 2 > INF:
            raise nx.NetworkXUnbounded("Infinite capacity path, flow unbounded above.")
        flow_value += this_flow

    R.graph["flow_value"] = flow_value
    return R
