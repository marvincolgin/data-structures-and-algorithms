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

    def pop(self) -> str:
        val = self.peek()
        if val != '':
            self._data.remove(val)
        return val

    def push(self, val: str) -> bool:
        self._data.insert(val)
        return True

    def peek(self) -> str:
        # not going to do it...
        # return self._data and self.data.head
        if self._data.head is not None:
            return self._data.head.value
        return ''

# *********************************
class Queue():


    def __init__(self):
        self._data = LinkList()

    def enqueue(val) -> bool:
       # Add a value to the queue
       return self._data.append(val)

    def dequeue(val) -> bool:
       # Remove entry from queue with a given value
       # NOTE: will only remove the first element found with val
       return self._data.remove(val)

    def peek() -> str:
       # Get value from the head of the queue (without removing it)
       if (self.
       pass

