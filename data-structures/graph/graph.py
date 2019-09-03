import os,sys,inspect
cwd = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.insert(0, cwd)
# sys.path.insert(0, cwd+'/../../data-structures/tree')
sys.path.insert(0, cwd+'/../../data-structures/stacks_and_queues')
from stacks_and_queues import Stack
from typing import List, Any, Optional
from collections import deque


class Vertex:
    def __init__(self, value: Any):
        self.value = value
        self.neighbors: List[Edge] = []  # noqa E701
        self.visited = False

    def __str__(self):
        return("value:", ''.join(self.value))


class Edge:
    def __init__(self, vertex: Vertex, weight=0):
        self.vertex = vertex
        self.weight = weight


class Graph:

    # internal data-struct for storing vertexes as list
    _vertexes: List[Vertex]

    def __init__(self):
        self._vertexes = []

    def __len__(self) -> int:
        # Returns the total number of nodes in the graph
        # Structure and Testing
        return len(self._vertexes)

    def add_vertex(self, value) -> Vertex:
        # Adds a new node to the graph
        vert = Vertex(value)
        self._vertexes.append(vert)
        return vert

    def add_edge(self, vert1: Vertex, vert2: Vertex, weight=0.0):
        # Adds a new edge between two nodes in the graph
        # Both nodes should already be in the Graph
        if vert1 in self._vertexes and vert2 in self._vertexes:
            vert1.neighbors.append(Edge(vert2, weight))

    def get_neighbors(self, vertex: Vertex) -> List[Edge]:
        # return a list of Edge classes which connet to neighbors
        return vertex.neighbors

    def get_vertexes(self) -> Optional[List[Vertex]]:
        # Returns all of the nodes in the graph as a collection
        return self._vertexes or None

    def breadth_first(self, root, action_func):
        # traverse through the graph, breadth-first order
        # @TODO: Since we are using a set() for to_reset(), we could
        # get rid of the .visited flag

        # init python queue class
        q = deque()

        # push initial object into queue
        q.appendleft(root)

        # Init our reset list
        to_reset = set()

        # While there are items in Que
        while q:

            # Get the current, mark as visited and add to reset
            current = q.pop()
            current.visited = True
            to_reset.add(current)

            # Call our Action function with the "Edge", which will have weight
            action_func(current)

            # Iterate through all the edge-connections to neighbors
            for edge in current.neighbors:
                if not edge.vertex.visited:
                    q.appendleft(edge.vertex)

        # reset visited flag for all vertexes visisted
        for vertex in to_reset:
            vertex.visited = False

    def depth_first_recursive(self, root: Vertex, action_func: Any) -> None:
        # traverse through the graph, depth-first order

        # Validate Input
        if not root or not isinstance(root, Vertex):
            raise EValueError("@param root must be a valid Vertex object")

        # Init internal data-struct
        visited = set()

        # Worker func for recursion
        def _visit(vertex):
            nonlocal visited, action_func

            # Check if we've seen this before
            if vertex in visited:
                return

            # Perform Action
            action_func(vertex.value)

            # Loop through connections
            for edge in vertex.neighbors:
                _visit(edge.vertex)

        # Prime Recursion
        _visit(root)

    def depth_first(self, root: Vertex, action_func: Any) -> None:
        # traverse through the graph, depth-first order

        # Validate Input
        if not root or not isinstance(root, Vertex):
            raise EValueError("@param root must be a valid Vertex object")

        # Init internal data-structs
        visited = set()
        # stack = Stack() @TODO: !!!Bug in my stack and last element of type string!!!
        stack = deque()


        # set initial vertex
        stack.append(root)

        # Stack will contain a lsit
        while stack:
            vertex = stack.pop()

            visited.add(vertex)
            action_func(vertex.value)

            for edge in vertex.neighbors:
                if not edge.vertex in visited:
                    stack.append(edge.vertex)


