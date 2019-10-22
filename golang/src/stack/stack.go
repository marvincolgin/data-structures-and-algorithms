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
func (stack *Stack) Pop() (bool, interface{}) {
	b, val := stack._data.Peek()
	if b {
		stack._data.Remove(val)
	}
	return b, val
}

// Push an item to top of Stack
func (stack *Stack) Push(val interface{}) bool {
	stack._data.Insert(val)
	return true
}

// Peek an item at top of Stack
func (stack *Stack) Peek() (bool, interface{}) {
	return stack._data.Peek()
}
