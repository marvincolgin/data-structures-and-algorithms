package stack

import (
	"fmt"
	"reflect"
	"testing"
)

func HelperStackAddLots() Stack {
	stack := Stack{}
	stack.Push("pao de queijo")
	stack.Push("pappa sandwich")
	stack.Push("banana")
	return stack
}

func TestCanCreate(t *testing.T) {
	stack := Stack{}
	if reflect.TypeOf(stack) != reflect.TypeOf((*Stack)(nil)).Elem() {
		t.Error("reflect.TypeOf(stack)!='Stack', actual=", reflect.TypeOf(stack))
	}
}

func TestPush(t *testing.T) {
	stack := Stack{}
	stack.Push("pao de queijo")
	ab, as := stack.Peek()
	eb, es := true, "pao de queijo"

	if ab != eb {
		t.Error("TestPush(), actual:", ab, " expected:", eb)
	}

	if as != es {
		t.Error("TestPush(), actual:", as, " expected:", es)
	}
}

func TestCount(t *testing.T) {
	stack := HelperStackAddLots()
	ai := stack.Count()
	ei := 3
	if ai != ei {
		t.Error("TestCount(), actual:", ai, " expected:", ei)
	}
}

func TestPop(t *testing.T) {
	stack := HelperStackAddLots()
	eb, es := true, "banana"
	ab, as := stack.Pop()
	if as != es {
		t.Error("TestPop(), actual:", as, " expected:", es)
	}
	if ab != eb {
		t.Error("TestPop(), actual:", ab, " expected:", eb)
	}

	ei := 2
	ai := stack.Count()
	if ai != ei {
		t.Error("TestPop(), actual:", ai, " expected:", ei)
	}
}

func TestPopEmpty(t *testing.T) {
	stack := HelperStackAddLots()

	// Pop all of the items
	for i := 0; i < stack.Count()+5; i++ {
		// eb, es := false, interface{}(nil)
		// ab, as := stack.Pop()

		ab, val := stack.Pop()
		as := fmt.Sprintf("%v", val)

		eb := true
		es := ""
		if i == 0 {
			es = "banana"
		} else if i == 1 {
			es = "pappa sandwich"
		} else if i == 2 {
			es = "pao de queijo"
		} else {
			// This is going past the number in the list
			eb = false
			es = ""
		}

		if ab != eb {
			t.Error("TestPop(), actual:", ab, " expected:", eb)
		}
		if as != es {
			t.Error("TestPop(), actual:", as, " expected:", es)
		}

	}

}

/*
def test_stack_empty_after_pops():
    # STACK: empty a stack after multiple pops
    stack = helper_stack_addlots()
    for x in range(stack.count()-1):
        stack.pop()
    expected = 1
    actual = stack.count()
    assert expected == actual

    stack.pop()
    actual = stack.count()
    expected = 0
    assert expected == actual


def test_stack_peek():
    # STACK: peek the next item on the stack
    stack = helper_stack_addlots()
    expectedBool = True
    expectedStr = 'banana'
    actualBool, actualStr = stack.peek()
    assert actualBool == expectedBool
    assert actualStr == expectedStr
*/
