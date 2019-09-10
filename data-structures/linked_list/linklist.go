package linklist

import (
	"fmt"
	"os"
	"strings"
)

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

// toStr dump list to string
func (list *LinkList) toStr() string {

	// # c,cnt are limiters to make sure we don't go run away
	// # yes, we need cnt=self.count() and not -1, as we walk off list
	c, cnt := 0, list.Count()
	buf := ""
	ptr := list.head
	for ptr != nil {
		s := fmt.Sprintf("%v", ptr.value)
		buf = buf + s + ","
		ptr = ptr.next
		c++
		if c > cnt {
			fmt.Fprintf(os.Stderr, "WAIT!!! Forever Loop!\nRecursive LinkList/Node\nbuf:[{buf}]")
			os.Exit(1)
		}
	}

	if strings.HasSuffix(buf, ",") {
		buf = buf[:len(buf)-1]
	}

	return buf
}

// Count the number of items
func (list *LinkList) Count() int {
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
