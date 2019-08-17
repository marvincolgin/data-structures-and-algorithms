import sys
sys.path.insert(0, '../linked_list')
from link_list import LinkList
import json


class HashTable():
    # Big O time == O(1)
    # :: worst case is O(n), if small hash array or terrible collisions


    # storage for HashTable
    _data = []


    def __init__(self, hashtableSize = 1024):
        # create with hashTableSize
        self._data = [None] * hashtableSize


    def _makePayload(self, name, value):
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


    def _get_callbackcompare(self, payload, val) -> bool:
        # func passed to LinkList compare
        return payload.get('name') == val


    def add(self, name, value):
        # accepts name/value pair and adds them to the hashtabl
        # if there are collisions, then they will be handled
        # by using a linked-list

        hash = self._makeHash(name)
        hashIdx = self._getHashIndex(hash)

        elem = self._data[hashIdx]
        payload = self._makePayload(name, value)

        if elem == None:
            elem = LinkList()
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
        if elem == None:
            raise ValueError('Not found')


        try:
            payload_dict = elem.get_callbackCompare(self._get_callbackcompare, name)
            return payload_dict.get('value')
        except Exception:
            raise Exception('Not found')


    def contains(self, name) -> bool:
        # returns true|false if the name is in the hashtable

        try:
            _ = self.get(name)
            return True
        except ValueError:
            return False

