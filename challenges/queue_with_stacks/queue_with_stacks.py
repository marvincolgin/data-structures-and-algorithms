import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir+'\\..\\data-structures\\stacks_and_queues')
p = parentdir+'\\..\\data-structures\\linked_list'
# r:\bps-web\cf-401\data-structures-and-algorithms\challenges\..\data-structures\linked_list\link_list.py
print(p)
sys.path.insert(0,p)

from stacks_and_queues import Stack


class PseudoQueue(object):

    # internal stack obj
    _data = None

    def __init__(self):
        # create Stack for internal data-struct
        self._data = Stack()

    def count(self):
        # pass through method to underlying data struct
        # BigO == O(n)
        return self._data.count()

    def enqueue(self, val: str) -> bool:
        # enqeue a value at the end queue
        # BigO == O(1)

        self._data.push(val)
        return True

    def dequeue(self) -> (str, bool):
        # dequeue from head of queue
        # BigO == O(n)
        # Algo: use a second stack, as we need the bottom element on the first stack
        # so we are going to unload the first stack, into a temp stack, in order to
        # get at the bottom element of the first, then rebuild it from temp to first-stack

        retStr = ''
        retBool = False

        # Empty List? Early return!
        b, s = self._data.peek()
        if not b:
            return retStr, retBool

        # reverse the primary stack into temp stack
        tempStack = Stack()
        while True:
            b, s = self._data.peek()
            if b == False:
                break
            val = self._data.pop()
            tempStack.push(val)

        # top element on tempstack is the bottom of the primary data stack
        retStr = tempStack.pop()

        # reverse the temp stack back to the primary stack
        while True:
            b, s = tempStack.peek()
            if b == False:
                break
            val = tempStack.pop()
            self._data.push(val)

        return retStr, True
