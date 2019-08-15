import pytest
import random
from quick_sort import quick_sort


def test_func_exists():
    quick_sort([1])

"""
def test_sort():
    input = [5,15,3,9,10]
    actual = quick_sort(input)
    expected = [3,5,9,10,15]
    # assert actual == expected
    assert True == False
"""

def test_sort():
    input = [1, 5, 3, 2, 4]
    actual = quick_sort(input)
    expected = [1, 2, 3, 4, 5]
    assert actual == expected


def test_all_same():
    input = [3, 3, 3, 3, 3, 3, 3]
    actual = quick_sort(input)
    expected = [3, 3, 3, 3, 3, 3, 3]
    assert actual == expected


def test_sort_zero():
    with pytest.raises(Exception):
        quick_sort([])


def test_sort_lots():
    input = []
    for x in range(1000):
        input.append(random.randint(1, 1000))

    actual = quick_sort(input)
    expected = input
    expected.sort()

    assert actual == expected
