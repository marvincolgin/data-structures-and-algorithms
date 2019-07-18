import sys
sys.path.insert(0, '../linked_list')
from link_list import LinkList


# ********************************
class Stack():

    _data = None

    def __init__(self):
        self._data = LinkList()
        pass

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
