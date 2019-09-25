import pytest
import random
from insertion_sort import insertion_sort


def test_func_exists():
    insertion_sort([1])


def test_sort():
    input = [1,5,3,2,4]
    actual = insertion_sort(input)
    expected = [1,2,3,4,5]
    assert actual == expected


def test_all_same():
    input = [3,3,3,3,3,3,3]
    actual = insertion_sort(input)
    expected = [3,3,3,3,3,3,3]
    assert actual == expected


def test_sort_zero():
    with pytest.raises(Exception):
        insertion_sort([])


def test_sort_lots():
    input = []
    for x in range(1000):
        input.append(random.randint(1,1000))

    actual = insertion_sort(input)
    expected = input
    expected.sort()

    assert actual == expected
