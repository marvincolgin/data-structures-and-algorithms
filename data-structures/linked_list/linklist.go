package linklist

//import (
//	"fmt"
//)

// LinkNode this is the internal object for individual link-nodes
type LinkNode struct {
	value interface{}
	next  *LinkNode
	prev  *LinkNode
}

// Init constructor for the object
func (node *LinkNode) Init(value interface{}) {
	node.value = value
	node.next = nil
	node.prev = nil
}

// LinkList is the internal data-structure
type LinkList struct {
	head *LinkNode
}

// Init constructor
func (list *LinkList) Init() {
	list.head = nil
}

// ListCount the number of items
func (list *LinkList) ListCount() int {
	cur := list.head

	c := 0
	for cur != nil {
		c++
		cur = cur.next
	}

	return c
}

// Append a value into LinkList
func (list *LinkList) Append(value interface{}) bool {

	// Walk to end of list
	prev, cur := (*LinkNode)(nil), list.head
	for cur != nil {
		prev = cur
		cur = cur.next
	}

	// create the node and add it to the end
	node := LinkNode{value: value}

	if prev == nil {
		list.head = &node
	} else {
		prev.next = &node
	}

	return true
}
