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
