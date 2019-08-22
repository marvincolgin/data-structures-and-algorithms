import pytest
from left_join import left_join
from hashtable import HashTable  # noqa E402


def test_func_exists():
    left_join(HashTable(), None)


def test_func_secondhashisnone():
    expected = []
    actual = left_join(HashTable(), None)
    assert expected == actual


def test_func_onematch_onedoesnt():

    h1 = HashTable()
    h1.add('fond', 'enamored')
    h1.add('wrath', 'anger')

    h2 = HashTable()
    h2.add('fond', 'averse')

    expected = [
        {'word': 'fond', 'synonym': 'enamored', 'antonym': 'averse' },  # noqa: E202
        {'word': 'wrath', 'synonym': 'anger', 'antonym': None }         # noqa: E202
    ]
    actual = left_join(h1, h2)
    assert expected == actual


def test_func_fullsample():
    h1 = HashTable()
    h1.add('fond', 'enamored')
    h1.add('wrath', 'anger')
    h1.add('diligent', 'employed')
    h1.add('outfit', 'garb')
    h1.add('guide', 'usher')

    h2 = HashTable()
    h2.add('fond', 'averse')
    h2.add('wrath', 'delight')
    h2.add('diligent', 'idle')
    h2.add('guide', 'follow')
    h2.add('flow', 'jam')

    expected = [
        {'word': 'diligent', 'synonym': 'employed', 'antonym': 'idle',    },  # noqa E202
        {'word': 'outfit',   'synonym': 'garb',     'antonym': None,      },  # noqa E202
        {'word': 'fond',     'synonym': 'enamored', 'antonym': 'averse',  },  # noqa E202
        {'word': 'guide',    'synonym': 'usher',    'antonym': 'follow',  },  # noqa E202
        {'word': 'wrath',    'synonym': 'anger',    'antonym': 'delight', }   # noqa E202
    ]

    actual = left_join(h1, h2)
    assert expected == actual
