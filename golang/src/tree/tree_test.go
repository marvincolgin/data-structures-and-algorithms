package tree

import (
	"reflect"
	"testing"
)

func HelperAddLots() BinaryTree {
	one := NewNode(1)
	two := NewNode(2)
	three := NewNode(3)
	four := NewNode(4)
	five := NewNode(5)
	six := NewNode(6)
	seven := NewNode(7)
	eight := NewNode(8)
	nine := NewNode(9)

	one.left = &two
	one.right = &three
	three.left = &four
	three.right = &five
	two.left = &six
	six.right = &seven
	seven.left = &eight
	seven.right = &nine

	retval := NewBinaryTree(nil)
	retval.root = &one

	return retval
}

func TestCanCreate(t *testing.T) {
	tree := NewBinaryTree(nil)
	if reflect.TypeOf(tree) != reflect.TypeOf((*BinaryTree)(nil)).Elem() {
		t.Error("TestCanCreate() reflect.TypeOf(tree)!='BinaryTree', actual=", reflect.TypeOf(tree))
	}
}

func TestTraversePre(t *testing.T) {
	tree := HelperAddLots()
	expected := []int{1, 2, 6, 7, 8, 9, 3, 4, 5}
	actual := tree.ReturnAsArr(TraversalOrderPre)

	actualAsInt := make([]int, len(actual))
	for i := range actual {
		actualAsInt[i] = actual[i].(int)
	}

	if !reflect.DeepEqual(expected, actualAsInt) {
		t.Error("TestTraversePre(), actual:", actualAsInt, " expected:", expected)
	}
}

func TestTraverseIn(t *testing.T) {
	tree := HelperAddLots()
	expected := []int{6, 8, 7, 9, 2, 1, 4, 3, 5}
	actual := tree.ReturnAsArr(TraversalOrderIn)

	actualAsInt := make([]int, len(actual))
	for i := range actual {
		actualAsInt[i] = actual[i].(int)
	}

	if !reflect.DeepEqual(expected, actualAsInt) {
		t.Error("TestTraverseIn(), actual:", actualAsInt, " expected:", expected)
	}
}

func TestTraversePost(t *testing.T) {
	tree := HelperAddLots()
	expected := []int{8, 9, 7, 6, 2, 4, 5, 3, 1}
	actual := tree.ReturnAsArr(TraversalOrderPost)

	actualAsInt := make([]int, len(actual))
	for i := range actual {
		actualAsInt[i] = actual[i].(int)
	}

	if !reflect.DeepEqual(expected, actualAsInt) {
		t.Error("TestTraversePost(), actual:", actualAsInt, " expected:", expected)
	}
}

func TestAddRoot(t *testing.T) {
	tree := NewBinaryTree(nil)
	tree.Add("apple")

	as := tree.root.Val
	es := "apple"

	if as != es {
		t.Error("TestAdd(), actual:", as, " expected:", es)
	}
}

func TestAddSmaller(t *testing.T) {
	tree := NewBinaryTree(nil)
	tree.Add(50)
	tree.Add(25)

	ai := tree.root.Val
	ei := 50
	if ai != ei {
		t.Error("TestAddSmaller(), actual:", ai, " expected:", ei)
	}

	ai = tree.root.left.Val
	ei = 25
	if ai != ei {
		t.Error("TestAddSmaller(), actual:", ai, " expected:", ei)
	}
}

func TestAddLarger(t *testing.T) {
	tree := NewBinaryTree(nil)
	tree.Add(50)
	tree.Add(75)

	ai := tree.root.Val
	ei := 50
	if ai != ei {
		t.Error("TestAddLarger(), actual:", ai, " expected:", ei)
	}

	ai = tree.root.right.Val
	ei = 75
	if ai != ei {
		t.Error("TestAddLarger(), actual:", ai, " expected:", ei)
	}
}

func TestContains(t *testing.T) {
	tree := NewBinaryTree(nil)
	tree.Add(50)
	ab := tree.Contains(50)
	eb := true
	if ab != eb {
		t.Error("TestContains(), actual:", ab, " expected:", eb)
	}
}

func TestContainsEmpty(t *testing.T) {
	tree := NewBinaryTree(nil)
	ab := tree.Contains(50)
	eb := false
	if ab != eb {
		t.Error("TestContainsEmpty(), actual:", ab, " expected:", eb)
	}
}

func TestContainsNotFound(t *testing.T) {
	tree := NewBinaryTree(nil)
	tree.Add(50)
	ab := tree.Contains(150)
	eb := false
	if ab != eb {
		t.Error("TestContainsEmpty(), actual:", ab, " expected:", eb)
	}
}

/*
def test_comparison_func_default():
    tree = BinarySearchTree()
    tree.add('1')
    tree.add('11')
    tree.add('111')
    tree.add('2')
    tree.add('22')
    tree.add('222')
    tree.add('3')
    tree.add('33')
    tree.add('333')
    expected = [ '1', '11', '111', '2', '22', '222', '3', '33', '333']
    actual = tree.returnAsArr(TraverseMethod.IN_ORDER)
    assert expected == actual


def test_comparison_func_userdef():

    def comparison_func(val1, val2, CS : ComparisonSign):
        # default comparison function

        print(f'comp() val1:[{val1}] val2:[{val2}] cs:[{CS}]')

        if CS == ComparisonSign.EQUAL:
            return int(val1) == int(val2)
        if CS == ComparisonSign.LESS:
            return int(val1) < int(val2)
        if CS == ComparisonSign.GREATER:
            return int(val1) > int(val2)
        return False  # Never get here

    tree = BinarySearchTree(comparison_func)
    tree.add('1')
    tree.add('11')
    tree.add('111')
    tree.add('2')
    tree.add('22')
    tree.add('222')
    tree.add('3')
    tree.add('33')
    tree.add('333')
    expected = [ '1', '2', '3', '11', '22', '33', '111', '222', '333' ]
    actual = tree.returnAsArr(TraverseMethod.IN_ORDER)
    assert expected == actual

def test_add_X_random():

    vals = []
    tree = BinarySearchTree()
    for j in range(50):

        # Generate a list of X elements (not duplicate)
        while True:
           x = str(random.randint(1,200))
           try:
               noused = vals.index(x)
           except:
               # No Found
               break

        vals.append(x)
        tree.add(x)

    actual = tree.returnAsArr(TraverseMethod.IN_ORDER)

    vals.sort()
    expected = vals

    assert expected == actual
*/
