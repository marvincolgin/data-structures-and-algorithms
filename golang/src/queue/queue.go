package queue

import (
	"linklist"
)

// Queue implementation of LIFO
type Queue struct {
	_data linklist.LinkList
}

// Init inistantiate the stuct
func (queue *Queue) Init() {
	queue._data = linklist.LinkList{}
}

// Count the number of items in linklist
func (queue *Queue) Count() int {
	return queue._data.Count()
}

// ToStr return the Queue as a String
func (queue *Queue) ToStr() string {
	return queue._data.ToStr()
}

// Enqueue to add a value to the queue
func (queue *Queue) Enqueue(val interface{}) bool {
	// Add a value to the queue
	return queue._data.Append(val)
}

// Dequeue to remove a specific value from the Qeueue
func (queue *Queue) Dequeue(val interface{}) bool {
	// Remove entry from queue with a given value
	// NOTE: will only remove the first element found with val
	return queue._data.Remove(val)
}

// Peek at the front value in the Queue
func (queue *Queue) Peek() (bool, interface{}) {
	// Get value from the head of the queue (without removing it)
	return queue._data.Peek()
}
