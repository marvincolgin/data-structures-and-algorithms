import sys
sys.path.insert(0, '../../data-structures/graph')
from typing import List, Any, Optional, Tuple
from graph import Graph # noqa E402


def get_edges(graph: Graph, path_ro: List) -> Tuple[bool, float]:
    # identify if a given path exists through the Graph
    # where path is a given list of values
    # @path_ro will be treated as read-only

    # Input Validation
    if not graph or not isinstance(graph, Graph):
        raise ValueError("@param 'graph': must be an instance of Graph.")
    if not path_ro or not isinstance(path_ro, List):
        raise ValueError("@param 'path_ro': must be an instance of List with entries.")

    # Bad Return
    defaultReturn = [False, 0.0]

    # Create local copy, as I don't want to mutate
    path = path_ro

    # Find Start in Graph (BigO time==V)
    found = False
    for v in graph._vertexes:
        if v.value == path[0]:
            _ = path.pop(0)
            found = True
            break
    if not found:
        return defaultReturn

    # Init
    cur = v
    cost = 0.00

    # Path is our queue of vertex values, as a route through the graph
    while path:

        # mutating path allows us to treat it as queue
        target = path.pop(0)

        # determine if the target exists as a value in the list[edge/vertex]
        found = False
        for edge in cur.neighbors:
            if edge.vertex.value == target:
                cur = edge.vertex
                cost += edge.weight
                found = True
                break
        if not found:
            return defaultReturn

    return [True, cost]
