import pytest
from hashtable import HashTable

def test_exists():
    assert HashTable

@pytest.mark.skip()
def test_get_missing():
    ht = HashTable()


    # do this or test for return of None if you go that way
    with pytest.raises(ValueError):
        ht.get('spam')

@pytest.mark.skip()
def test_add():
    ht = HashTable()
    ht.add('spam','eggs')

    assert ht.get('spam') == 'eggs'

@pytest.mark.skip()
def test_contains():
    ht = HashTable()
    ht.add('spam','eggs')
    assert ht.contains('spam')

@pytest.mark.skip()
def test_not_contains():
    ht = HashTable()
    assert not ht.contains('spam')

@pytest.mark.skip()
def test_hash_same():
    ht = HashTable()
    assert ht.hash('taco') == ht.hash('taco')

@pytest.mark.skip()
def test_hash_in_range():
    ht = HashTable()
    assert  0 <= ht.hash('eggs') < len(ht.buckets)


@pytest.mark.skip()
def test_hash_different():
    ht = HashTable()
    assert not ht.hash('taco') == ht.hash('bell')


@pytest.mark.skip()
def test_collision():
    ht = HashTable()
    ht.add('spam','spammy stuff')
    ht.add('maps', 'mappy stuff')
    assert ht.get('spam') == 'spammy stuff'
    assert ht.get('maps') == 'mappy stuff'


