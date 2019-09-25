import sys
sys.path.insert(0, '../linked_list')
from link_list import LinkList  # noqa E402
import json  # noqa E402


class HashTable():
    # Big O time == O(1)
    # :: worst case is O(n), if small hash array or terrible collisions

    # storage for HashTable
    _data = []

    def __init__(self, hashtableSize=1024):
        # create with hashTableSize
        self._data = [None] * hashtableSize

    def _makePayload(self, name, value) -> dict:
        # return dict of name/value pair
        return({'name': name, 'value': value})

    def _makeHash(self, name) -> int:
        # create a hash based on the name to be added to hashtable
        # this is a silly hash, as it's just for experiment and
        # gives us the ability to easily create collisions. Live
        # code should use something more sophisticated

        char_sum = sum([ord(char) for char in name])

        # prime numbers "make it better" (tm)
        prime_number = 599

        hash = char_sum * prime_number

        return hash

    def _getHashIndex(self, hash: int) -> int:
        # get the index into the hash-table for a given hash value

        return hash % len(self._data)

    def _hashtable_compare_func(self, payload1, payload2) -> bool:
        # func passed to LinkList compare

        # sometimes we will compare our own payload
        # other times, it's just the varname coming in as payload2
        if isinstance(payload2, dict):
            retVal = payload1.get('name') == payload2.get('name')
        else:
            retVal = payload1.get('name') == payload2

        return retVal

    def add(self, name, value):
        # accepts name/value pair and adds them to the hashtable
        # if there are collisions, then they will be handled
        # by using a linked-list

        hash = self._makeHash(name)
        hashIdx = self._getHashIndex(hash)

        elem = self._data[hashIdx]
        payload = self._makePayload(name, value)

        if elem is None:
            elem = LinkList(self._hashtable_compare_func)
            elem.insert(payload)
            self._data[hashIdx] = elem
        else:
            if not elem.includes(payload):
                elem.insert(payload)
            else:
                raise ValueError('Already added to hashtable')

    def get(self, name):
        # returns value in hashtable for a given name
        # if the value is not found, and exception will be raised

        hash = self._makeHash(name)
        hashIdx = self._getHashIndex(hash)

        elem = self._data[hashIdx]
        if elem is None:
            raise ValueError('Not found')

        try:
            payload_dict = elem.get(name)
            return payload_dict.get('value')
        except Exception:
            raise ValueError('Not found')

    def delete(self, name):
        # remove an entry in the hashtable

        found = False
        try:
            found = self.contains(name)
        except ValueError:
            raise ValueError(f'Name:[{name}] does not exist.')

        if found:
            hash = self._makeHash(name)
            hashIdx = self._getHashIndex(hash)

            elem = self._data[hashIdx]
            if elem is None:
                raise ValueError(f'Name:[{name}] entry into HashTable is None.')

            b = elem.remove(name)

    def update(self, name, value):
        # updates an entry in the hashtable with a new value

        if not self.contains(name):
            raise ValueError(f'Name:[{name}] does not exist.')

        self.delete(name)
        self.add(name, value)

    def contains(self, name) -> bool:
        # returns true|false if the name is in the hashtable

        try:
            _ = self.get(name)
            return True
        except ValueError:
            return False

    def export_keys(self) -> list:
        # exports a list of all the keys in hashtable

        retArr = []
        def touch_node(value):
            retArr.append(value)

        for linklist in self._data:
            if linklist:
                linklist.traverse(touch_node)

        return retArr
