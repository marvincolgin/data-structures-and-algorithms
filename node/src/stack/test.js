var chai = require('chai');
var expect = chai.expect; // we are using the 'expect' style of Chai

var Stack = require('./stack').Stack


function HelperStackAddLots() {
	stack = new Stack()
	stack.push("pao de queijo")
	stack.push("pappa sandwich")
	stack.push("banana")
	return stack
}

//s = HelperStackAddLots()
let s = new Stack()
console.log(s)

describe('new Stack()', function() {
   it('new stack()', function() {
      expect(new Stack()).to.be.an.instanceof(Stack);
   })
})

/*

func TestCanCreate(t *testing.T) {
	stack := Stack{}
	if reflect.TypeOf(stack) != reflect.TypeOf((*Stack)(nil)).Elem() {
		t.Error("reflect.TypeOf(stack)!='Stack', actual=", reflect.TypeOf(stack))
	}
}

func TestPushAndPeek(t *testing.T) {
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
	for i, len := 0, stack.Count(); i < len; i++ {

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
			t.Error("TestPop(), we should never be here i:", i, " len:", len)
		}

		if ab != eb {
			t.Error("TestPop(), actual:", ab, " expected:", eb)
		}
		if as != es {
			t.Error("TestPop(), actual:", as, " expected:", es)
		}
	}

	// Make sure it's reporting 0 for count
	len := stack.Count()
	if len != 0 {
		t.Error("TestPop(), len!=0, len:", len)
	}

	// Pop one more to test error
	eb, ev := false, interface{}(nil)
	ab, av := stack.Pop()
	if ab != eb {
		t.Error("TestPop(), actual:", ab, " expected:", eb)
	}
	if av != ev {
		t.Error("TestPop(), actual:", av, " expected:", ev)
	}
}
*/