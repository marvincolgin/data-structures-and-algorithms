package linklist

import (
	"testing"
)

func TestNode(t *testing.T) {

	node := LinkNode{value: "test"}
	if node.value != "test" {
		t.Error("node.value shuold be 'test', but it is ", node.value)
	}
}

func TestCountEmpty(t *testing.T) {
	list := LinkList{}
	if list.ListCount() != 0 {
		t.Error("list != 0, actual:", list.ListCount())
	}
}

func TestAppend(t *testing.T) {
	list := LinkList{}
	list.Append('1')

	if list.head == nil {
		t.Error("list.head is nil")
	}

	if list.ListCount() != 1 {
		t.Error("list.count() != 1, actual:", list.ListCount())
	}
}

func TestAppendMany(t *testing.T) {
	list := LinkList{}
	list.Append('0')
	list.Append('1')
	list.Append('2')
	list.Append('3')
	list.Append('4')
	list.Append('5')
	list.Append('6')
	list.Append('7')
	list.Append('8')
	list.Append('9')

	if list.ListCount() != 10 {
		t.Error("list.count()!=10, actual:", list.ListCount())
	}

	if list.head.value != '9' {
		t.Error("value!=9, actual:", list.head.value)
	}

	/*
		    assert ll.count() == 10
		    assert ll.head.value == '9'
		    assert ll.head.next.value == '8'
		    assert ll.head.next.next.value == '7'
		    assert ll.head.next.next.next.value == '6'
		    assert ll.head.next.next.next.next.value == '5'
		    assert ll.head.next.next.next.next.next.value == '4'
		    assert ll.head.next.next.next.next.next.next.value == '3'
		    assert ll.head.next.next.next.next.next.next.next.value == '2'
		    assert ll.head.next.next.next.next.next.next.next.next.value == '1'
		    assert ll.head.next.next.next.next.next.next.next.next.next.value == '0'
			assert ll.head.next.next.next.next.next.next.next.next.next.next is None
	*/
}
