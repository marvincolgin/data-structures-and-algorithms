package stack

import (
	"linklist"
)

// Stack implementation of LIFO
type Stack struct {
	_data linklist.LinkList
}

// Init inistantiate the stuct
func (stack *Stack) Init() {
	stack._data = linklist.LinkList{}
}

// Count the number of items in linklist
func (stack *Stack) Count() int {
	return stack._data.Count()
}

// Pop an item from the front of the stack
func (stack *Stack) Pop() interface{} {
	b, val := stack._data.Peek()
	if b {
		stack._data.Remove(val)
	}
	return val
}

// Push an item to top of Stack
func (stack *Stack) Push(val interface{}) bool {
	stack._data.Insert(val)
	return true
}

/*
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
*/
