import networkx as nx
from networkx.algorithms.flow.utils import build_residual_network

__all__ = ["ford_fulkerson"]


def ford_fulkerson_core(R, s, t, cutoff):
    """Implementation of the Ford-Fulkerson algorithm."""
    R_succ = R.succ

    inf = R.graph["inf"]

    def augment(path):

        """Augment flow along a path from s to t."""
        # Determine the path residual capacity.
        flow = inf

        it = iter(path)
        u = next(it)
        for v in it:
            attr = R_succ[u][v]
            flow = min(flow, attr["capacity"] - attr["flow"])
            u = v
        if flow * 2 > inf:
            raise nx.NetworkXUnbounded("Infinite capacity path, flow unbounded above.")
        # Augment flow along the path.
        it = iter(path)
        u = next(it)
        for v in it:
            R_succ[u][v]["flow"] += flow
            R_succ[v][u]["flow"] -= flow
            u = v
        return flow

    def dfs():
        # print('Regular breadth-first search for an augmenting path.')
        """Regular breadth-first search for an augmenting path."""
        pred = {s: None}
        q = [s]
        while q:
            u = q.pop()
            for v, attr in R_succ[u].items():
                if v not in pred and attr["flow"] < attr["capacity"]:
                    pred[v] = u
                    if v == t:
                        return v, pred
                    q.append(v)
        return None, None

    # Look for shortest augmenting paths using breadth-first search.
    flow_value = 0
    while flow_value < cutoff:
        v, pred = dfs()
        if pred is None:
            break
        path = [v]
        # Trace a path from s to v.
        u = v
        while u != s:
            u = pred[u]
            path.append(u)
        path.reverse()

        flow_value += augment(path)

    return flow_value


def ford_fulkerson_impl(G, s, t, capacity, residual, cutoff):
    """Implementation of the Edmonds-Karp algorithm."""
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

    if cutoff is None:
        cutoff = float("inf")

    R.graph["flow_value"] = ford_fulkerson_core(R, s, t, cutoff)

    return R


def ford_fulkerson(
        G, s, t, capacity="capacity", residual=None, value_only=False, cutoff=None
):
    R = ford_fulkerson_impl(G, s, t, capacity, residual, cutoff)
    R.graph["algorithm"] = "ford_fulkerson"
    return R
