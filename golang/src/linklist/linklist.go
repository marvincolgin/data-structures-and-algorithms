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
	// @TODO: comparison_func func
}

// Init constructor
func (list *LinkList) Init( /* @TODO: comparison_func=nil */ ) {
	list.head = nil
	// @TODO: self.comparison_func = comparison_func
}

// toJSON will output the string in JSON format
func (list *LinkList) toJSON() string {
	// @TODO Get a module for this
	return ""
}

// ToStr dump list tos string
func (list *LinkList) ToStr() string {

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

// Insert a value into the link list
func (list *LinkList) Insert(value interface{}) bool {
	node := LinkNode{value: value}
	node.next = list.head
	list.head = &node
	return true
}

// Includes tests to see if a value exists
func (list *LinkList) Includes(value interface{}) bool {
	retVal := false

	cur := list.head
	for cur != nil {
		/*
			if list.comparison_func != nil {
				if list.comparison_func(cur.value, value) {
					retVal = true
					break
				}
			} else {
		*/
		if cur.value == value {
			retVal = true
			break
		}
		/*
			} */
		cur = cur.next
	}

	return retVal
}

// Get will traverse the list and determine if a value exists
func (list *LinkList) Get(value interface{}) interface{} {
	// @TODO: make this return a tuple with error-code
	cur := list.head
	for cur != nil {
		/*
			if list.comparison_func != nil {
				if list.comparison_func(cur.value, value) {
					return cur.value
				}
			} else {
		*/
		if cur.value == value {
			return cur.value
		}
		//		}
		cur = cur.next
	}
	return false
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

// Remove a node from a list, given a specific value
func (list *LinkList) Remove(value interface{}) bool {
	// BigO == O(n*2) ... I could eliminate self.includes(), but I think it's more readable
	// NOTE: only the first one found will be removed

	retVal := false
	if list.Includes(value) {
		prev, cur := (*LinkNode)(nil), list.head

		for cur != nil {

			found := false
			// if list.comparison_func != nil {
			// 	if self.comparison_func(cur.value, value):
			// 		found = True
			// } else  {
			if cur.value == value {
				found = true
			}
			// }

			if found {
				if prev == nil {
					list.head = cur.next
				} else {
					prev.next = cur.next
				}
				retVal = true
				break
			}

			prev = cur
			cur = cur.next
		}

	}

	return retVal
}

// Peek a value from the front of the list
func (list *LinkList) Peek() (bool, interface{}) {
	retVal := interface{}(nil)
	retBool := false
	if list.head != nil {
		retVal = list.head.value
		retBool = true
	}
	return retBool, retVal
}

// InsertBefore add a new node with the given newValue immediately BEFORE the node containg targetVal
func (list *LinkList) InsertBefore(targetVal, newVal interface{}, afterInstead bool) bool {
	// # note: this bevahoir can be modified by the bool afterInstead
	// # BigO == O(n)

	// walk the list to find it or the end
	found := false
	prev, cur := (*LinkNode)(nil), list.head
	for cur != nil {
		// @TODO convert to use comparison_func()
		if cur.value == targetVal {
			found = true
			break
		}
		prev = cur
		cur = cur.next
	}

	// # if found, put it in the chain, as a link right before the node containing value
	if found {
		node := LinkNode{value: newVal}
		if afterInstead {
			node.next = cur.next
			cur.next = &node
		} else {
			node.next = cur
			if prev == nil { // edge-case, if the targetVal is first node
				list.head = &node
			} else {
				prev.next = &node
			}
		}
	}

	return found
}

// InsertAfter add a new node with the given newValue immediately AFTER the node containg targetVal
func (list *LinkList) InsertAfter(targetVal, newVal interface{}) bool {
	// BigO == O(n)
	return list.InsertBefore(targetVal, newVal, true)
}

// KthFromEnd finds the Kth element from the end of the list and returns value for node
func (list *LinkList) KthFromEnd(k int) (bool, interface{}) {
	// BigO == O(n)

	// Only positive integers
	if k < 0 {
		return false, interface{}(nil)
	}

	ptrA := list.head
	ptrB := list.head

	// Walk ptrA out to "K" elements
	tooSmall := false
	c := 0
	for c < k-1 {
		if ptrA.next == nil {
			tooSmall = true
			break
		}
		ptrA = ptrA.next
		c = c + 1
	}
	if tooSmall {
		return false, interface{}(nil)
	}

	// Walk ptrA and ptrB out to the end of the list
	// ptrB will point to our requested node
	// note: for short lengths where the value is found before k elements, we are going to skip walking
	// ptrB until the difference between it and ptrA is "k"
	for ptrA.next != nil {
		ptrA = ptrA.next
		if c >= k {
			ptrB = ptrB.next
		}
		c = c + 1
	}

	return true, ptrB.value
}

// MergeList two lists together (zipper)
func (list *LinkList) MergeList(listA, listB LinkList) LinkList {
	// BigO == O(n)

	ptrA := listA.head
	ptrB := listB.head

	var prev *LinkNode
	for ptrA != nil || ptrB != nil {
		if ptrA != nil {
			prev = ptrA
			ptrA = ptrA.next
			prev.next = ptrB
		}
		if ptrB != nil {
			prev = ptrB
			ptrB = ptrB.next
			prev.next = ptrA
		}
	}

	return listA
}
