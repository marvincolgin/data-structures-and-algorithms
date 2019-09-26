package queue

import (
	"reflect"
	"strings"
	"testing"
)

func HelperQueueLots() Queue {
	q := Queue{}
	q.Enqueue("pao de queijo")
	q.Enqueue("pappa sandwidh")
	q.Enqueue("banana")
	q.Enqueue("crackers")
	q.Enqueue("strawberries")
	q.Enqueue("chocolate chips")
	return q
}

func TestCanCreate(t *testing.T) {
	queue := Queue{}
	if reflect.TypeOf(queue) != reflect.TypeOf((*Queue)(nil)).Elem() {
		t.Error("reflect.TypeOf(queue)!='Queue', actual=", reflect.TypeOf(queue))
	}
}

func TestEnqueue(t *testing.T) {
	q := Queue{}
	q.Enqueue("pao de queijo")
	ai := q.Count()
	ei := 1
	if ai != ei {
		t.Error("TestEnqueue(), actual:", ai, " expected:", ei)
	}
}

func TestEnqueueLots(t *testing.T) {
	q := HelperQueueLots()
	ai := q.Count()
	ei := 6
	if ai != ei {
		t.Error("TestEnqueueLots(), actual:", ai, " expected:", ei)
	}

}

func TestDequeueSuccess(t *testing.T) {
	q := HelperQueueLots()
	eb := true
	ab := q.Dequeue("banana")
	if ab != eb {
		t.Error("TestDequeueSuccess(), actual:", ab, " expected:", eb)
	}
	ei := 5
	ai := q.Count()
	if ai != ei {
		t.Error("TestDequeueSuccess(), actual:", ai, " expected:", ei)
	}
}

func TestDequeueError(t *testing.T) {
	q := HelperQueueLots()
	eb := false
	ab := q.Dequeue("somethingyouwontfind")
	if ab != eb {
		t.Error("TestDequeueSuccess(), actual:", ab, " expected:", eb)
	}
	ei := 6
	ai := q.Count()
	if ai != ei {
		t.Error("TestDequeueSuccess(), actual:", ai, " expected:", ei)
	}
}

func TestQueuePeek(t *testing.T) {
	q := HelperQueueLots()
	ab, as := q.Peek()
	eb := true
	es := "pao de queijo"
	if ab != eb {
		t.Error("TestQueuePeek(), actual:", ab, " expected:", eb)
	}
	if as != es {
		t.Error("TestQueuePeek(), actual:", as, " expected:", es)
	}
}

func TestQueuePeekEmpty(t *testing.T) {
	q := Queue{}
	ab, as := q.Peek()
	eb := false
	es := (interface{})(nil)
	if ab != eb {
		t.Error("TestQueuePeek(), actual:", ab, " expected:", eb)
	}
	if as != es {
		t.Error("TestQueuePeek(), actual:", as, " expected:", es)
	}
}

func TestQueueDequeueUntilEmpty(t *testing.T) {
	q := HelperQueueLots()
	arr := strings.Split(q.ToStr(), ",")
	for i, len := 0, q.Count(); i < len; i++ {
		ab := q.Dequeue(arr[i])
		eb := true
		if ab != eb {
			t.Error("TestQueueDequeueUntilEmpty(), actual:", ab, " expected:", eb)
		}
	}

	ai := q.Count()
	ei := 0
	if ai != ei {
		t.Error("TestQueueDequeueUntilEmpty(), actual:", ai, " expected:", ei)
	}

}
