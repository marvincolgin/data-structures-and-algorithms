import pytest
from graph import Graph, Vertex

"""
X vertex can be successfully added to the graph
X An edge can be successfully added to the graph
X A collection of all vertexes can be properly retrieved from the graph
X All appropriate neighbors can be retrieved from the graph
X Neighbors are returned with the weight between vertexes included
X The proper size is returned, representing the number of vertexes in the graph
X A graph with only one vertex and edge can be properly returned
X An empty graph properly returns null
"""


def test_exists():
    assert Graph
    assert Vertex


def test_add_single():
    g = Graph()
    blackberry = g.add_vertex('blackberry')
    assert isinstance(blackberry, Vertex)
    assert blackberry.value == 'blackberry'


def test_add_multiple():
    g = Graph()
    blackberry = g.add_vertex('blackberry')
    strawberry = g.add_vertex('strawberry')
    blueberry = g.add_vertex('blueberry')
    assert blackberry.value == 'blackberry'
    assert strawberry.value == 'strawberry'
    assert blueberry.value == 'blueberry'


def test_get_single():
    g = Graph()
    blackberry = g.add_vertex('blackberry')
    vertexes = g.get_vertexes()
    assert len(vertexes) == 1
    assert vertexes[0].value == 'blackberry'


def test_get_multiple():
    g = Graph()
    g.add_vertex('blackberry')
    g.add_vertex('strawberry')
    g.add_vertex('blueberry')
    vertexes = g.get_vertexes()
    assert len(vertexes) == 3
    assert {vertex.value for vertex in vertexes} == set(['blackberry', 'strawberry', 'blueberry'])  # noqa: 501


def test_length():
    g = Graph()
    g.add_vertex('blackberry')
    g.add_vertex('strawberry')
    assert len(g) == 2


def test_empty():
    g = Graph()
    assert g.get_vertexes() is None


def test_add_edge():
    g = Graph()
    blackberry = g.add_vertex('blackberry')
    strawberry = g.add_vertex('strawberry')
    g.add_edge(blackberry, strawberry, 15)
    blackberry_strawberry_edge = blackberry.neighbors[0]

    assert blackberry_strawberry_edge.vertex == strawberry
    assert blackberry_strawberry_edge.weight == 15
    assert len(strawberry.neighbors) == 0


def test_get_neighbors():
    g = Graph()
    blackberry = g.add_vertex('blackberry')
    strawberry = g.add_vertex('strawberry')
    blueberry = g.add_vertex('blueberry')
    g.add_edge(blackberry, strawberry, 15)
    g.add_edge(blackberry, blueberry, 12)

    neighbors = g.get_neighbors(blackberry)

    assert neighbors[0].vertex.value == 'strawberry'
    assert neighbors[0].weight == 15

    assert neighbors[1].vertex.value == 'blueberry'
    assert neighbors[1].weight == 12


def test_self_loop():
    g = Graph()
    blackberry = g.add_vertex('blackberry')
    g.add_edge(blackberry, blackberry)
    neighbors = g.get_neighbors(blackberry)

    assert neighbors[0].vertex.value == 'blackberry'
    assert neighbors[0].weight == 0

    vertexes = g.get_vertexes()
    assert [vertex.value for vertex in vertexes] == ['blackberry']


def test_breadth_first():
    g = Graph()
    blackberry = g.add_vertex('blackberry')
    strawberry = g.add_vertex('strawberry')
    blueberry = g.add_vertex('blueberry')
    g.add_edge(blackberry, strawberry, 15)
    g.add_edge(blackberry, blueberry, 12)

    visited = []

    def visit(vertex):
        visited.append(vertex.value)

    g.breadth_first(blackberry, visit)

    assert visited == ['blackberry', 'strawberry', 'blueberry']


def test_depth_first():
    graph = Graph()

    a = graph.add_vertex('a')
    b = graph.add_vertex('b')
    c = graph.add_vertex('c')
    d = graph.add_vertex('d')
    e = graph.add_vertex('e')
    f = graph.add_vertex('f')
    g = graph.add_vertex('g')
    h = graph.add_vertex('h')

    # Undirected Graph

    # A
    graph.add_edge(a, b)
    graph.add_edge(a, d)

    # B
    graph.add_edge(b, c)

    # C
    graph.add_edge(b, g)

    # D
    graph.add_edge(d, f)
    graph.add_edge(d, h)
    graph.add_edge(d, e)

    # E

    # F
    # No more undirected edges

    # G
    # No more undirected edges

    # H
    # No more undirected edges

    """
    # Directed Graph

    # A
    graph.add_edge(a, b)
    graph.add_edge(a, d)

    # B
    graph.add_edge(b, c)
    graph.add_edge(b, d)
    graph.add_edge(b, a)

    # C
    graph.add_edge(c, b)
    graph.add_edge(c, g)

    # D
    graph.add_edge(d, a)
    graph.add_edge(d, b)
    graph.add_edge(d, f)
    graph.add_edge(d, h)
    graph.add_edge(d, e)

    # E
    graph.add_edge(e, d)

    # F
    graph.add_edge(f, d)
    graph.add_edge(f, h)

    # H
    graph.add_edge(h, f)
    graph.add_edge(h, d)
    """

    def _visit(value):
        print(f'_visited()::value:', value)
        visited.append(value)

    # Recursive
    visited = []
    graph.depth_first_recursive(a, _visit)
    expected = ['a', 'b', 'c', 'g', 'd', 'f', 'h', 'e']
    assert visited == expected

    # Stack
    visited = []
    graph.depth_first(a, _visit)
    expected = ['a', 'd', 'e', 'h', 'f', 'b', 'g', 'c']
    assert visited == expected
