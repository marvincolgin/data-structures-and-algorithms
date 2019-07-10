from array_binary_search import array_binary_search


def test_function_exists():
    assert array_binary_search


def test_search_exists_firstidx():
    expected = 1
    actual = array_binary_search([1, 3, 5, 7, 9], 3)
    assert expected == actual


def test_search_exists2():
    expected = 3
    actual = array_binary_search([1, 3, 5, 7, 9], 7)
    assert expected == actual


def test_search_exists_lastidx():
    expected = 4
    actual = array_binary_search([1, 3, 5, 7, 9], 9)
    assert expected == actual


def test_search_noexists():
    expected = -1
    actual = array_binary_search([1, 2, 4, 7, 9], 5)
    assert expected == actual
