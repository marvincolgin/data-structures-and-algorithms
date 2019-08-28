import sys
sys.path.insert(0, '../../data-structures/graph')
from graph import Graph  # noqa E402
import pytest  # noqa 402
from get_edges import get_edges  # noqa 402


def test_invalid_input():
    with pytest.raises(ValueError):
        get_edges(None, [])

    with pytest.raises(ValueError):
        get_edges(Graph(), None)




def test_valid():

    g = Graph()
    sea = g.add_vertex('SEA')
    pdx = g.add_vertex('PDX')
    slc = g.add_vertex('SLC')
    lax = g.add_vertex('LAX')
    fla = g.add_vertex('FLA')

    g.add_edge(sea, pdx, 1)
    g.add_edge(pdx, sea, 1)

    g.add_edge(pdx, slc, 10)
    g.add_edge(slc, pdx, 10)

    g.add_edge(slc, lax, 100)
    g.add_edge(lax, slc, 100)

    g.add_edge(lax, fla, 1000)
    g.add_edge(fla, lax, 1000)

    path = ['SEA', 'PDX', 'SLC', 'LAX', 'FLA']
    actual = get_edges(g, path)
    expected = [True, 1111.0]

    assert actual == expected


def test_invalid():

    g = Graph()
    sea = g.add_vertex('SEA')
    pdx = g.add_vertex('PDX')
    slc = g.add_vertex('SLC')
    lax = g.add_vertex('LAX')
    fla = g.add_vertex('FLA')

    g.add_edge(sea, pdx, 1)
    g.add_edge(pdx, sea, 1)

    g.add_edge(pdx, slc, 10)
    g.add_edge(slc, pdx, 10)

    g.add_edge(slc, lax, 100)
    g.add_edge(lax, slc, 100)

    # Same as valid, but without this connection
    # g.add_edge(lax, fla, 1000)
    # g.add_edge(fla, lax, 1000)

    path = ['SEA', 'PDX', 'SLC', 'LAX', 'FLA']
    actual = get_edges(g, path)
    expected = [False, 0.0]

    assert actual == expected
