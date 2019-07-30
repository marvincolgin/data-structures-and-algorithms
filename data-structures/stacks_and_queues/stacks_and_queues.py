import sys
sys.path.insert(0, '../linked_list')
from link_list import LinkList


# ********************************
class Stack():

    _data = None

    def __init__(self):
        self._data = LinkList()

    def count(self) -> int:
        return self._data.count()

    def pop(self) -> object:
        b, val = self._data.peekHead()
        if b:
            self._data.remove(val)
        return val

    def push(self, val: object) -> bool:
        self._data.insert(val)
        return True

    def peek(self) -> [bool, object]:
        return self._data.peekHead()


# *********************************
class Queue():

    def __init__(self):
        self._data = LinkList()

    def count(self) -> int:
        return self._data.count()

    def toStr(self) -> str:
        return self._data.toStr()

    def enqueue(self, val) -> bool:
        # Add a value to the queue
        return self._data.append(val)

    def dequeue(self, val) -> bool:
        # Remove entry from queue with a given value
        # NOTE: will only remove the first element found with val
        return self._data.remove(val)

    def peek(self) -> [bool, object]:
        # Get value from the head of the queue (without removing it)
        return self._data.peekHead()
