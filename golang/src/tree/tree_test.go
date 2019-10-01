package tree

import (
	"reflect"
	"testing"
)

func HelperAddLots() BinaryTree {

	one := Node{1, nil, nil}
	two := Node{2, nil, nil}
	three := Node{3, nil, nil}
	four := Node{4, nil, nil}
	five := Node{5, nil, nil}
	six := Node{6, nil, nil}
	seven := Node{7, nil, nil}
	eight := Node{8, nil, nil}
	nine := Node{9, nil, nil}

	one.left = &two
	one.right = &three
	three.left = &four
	three.right = &five
	two.left = &six
	six.right = &seven
	seven.left = &eight
	seven.right = &nine

	retval := BinaryTree{}
	retval.root = &one

	return retval

}

func TestCanCreate(t *testing.T) {
	tree := BinaryTree{}
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
		t.Error("TestTraversePre(), actualAsInt:", actualAsInt, " expected:", expected)
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
		t.Error("TestTraverseIn(), actualAsInt:", actualAsInt, " expected:", expected)
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
		t.Error("TestTraversePost(), actualAsInt:", actualAsInt, " expected:", expected)
	}
}

/*
func TestContains(t *testing.T) {
	tree := BinaryTree{}
	tree.Add(50)
	ab := tree.Contains(50)
	eb := true
}
*/
/*

def test_contains_empty():
    tree = BinarySearchTree()
    assert tree.contains(50)==False

def test_add_empty():
    tree = BinarySearchTree()
    tree.add("apple")
    assert tree.root.value == "apple"

def test_add_smaller():
    tree = BinarySearchTree()
    tree.add(50)
    tree.add(25)
    assert tree.root.value == 50
    assert tree.root.left.value == 25

def test_add_larger():
    tree = BinarySearchTree()
    tree.add(50)
    tree.add(75)
    assert tree.root.value == 50
    assert tree.root.right.value == 75

def test_not_contains():
    tree = BinarySearchTree()
    tree.add(50)
    assert not tree.contains(150)

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
