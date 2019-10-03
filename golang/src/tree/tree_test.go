package tree

import (
	"math/rand"
	"reflect"
	"sort"
	"strconv"
	"testing"
)

func HelperAddLots() BinarySearchTree {
	one := NewNode("1")
	two := NewNode("2")
	three := NewNode("3")
	four := NewNode("4")
	five := NewNode("5")
	six := NewNode("6")
	seven := NewNode("7")
	eight := NewNode("8")
	nine := NewNode("9")

	one.left = &two
	one.right = &three
	three.left = &four
	three.right = &five
	two.left = &six
	six.right = &seven
	seven.left = &eight
	seven.right = &nine

	retval := NewBinarySearchTree(nil)
	retval.root = &one

	return retval
}

func TestCanCreate(t *testing.T) {
	tree := NewBinarySearchTree(nil)
	if reflect.TypeOf(tree) != reflect.TypeOf((*BinarySearchTree)(nil)).Elem() {
		t.Error("TestCanCreate() reflect.TypeOf(tree)!='BinarySearchTree', actual=", reflect.TypeOf(tree))
	}
}
func GetTypeArray(arr interface{}) reflect.Type {
	return reflect.TypeOf(arr).Elem()
}
func TestTraversePre(t *testing.T) {
	tree := HelperAddLots()

	var expected []interface{}
	expected = append(expected, "1", "2", "6", "7", "8", "9", "3", "4", "5")

	actual := tree.ReturnAsArr(TraversalOrderPre)

	if !reflect.DeepEqual(expected, actual) {
		t.Error("TestTraversePre(), actual:", actual, " expected:", expected)
	}
}

func TestTraverseIn(t *testing.T) {
	tree := HelperAddLots()

	var expected []interface{}
	expected = append(expected, "6", "8", "7", "9", "2", "1", "4", "3", "5")

	actual := tree.ReturnAsArr(TraversalOrderIn)

	if !reflect.DeepEqual(expected, actual) {
		t.Error("TestTraverseIn(), actual:", actual, " expected:", expected)
	}
}

func TestTraversePost(t *testing.T) {
	tree := HelperAddLots()

	var expected []interface{}
	expected = append(expected, "8", "9", "7", "6", "2", "4", "5", "3", "1")
	actual := tree.ReturnAsArr(TraversalOrderPost)

	if !reflect.DeepEqual(expected, actual) {
		t.Error("TestTraversePost(), actual:", actual, " expected:", expected)
	}
}

func TestAddRoot(t *testing.T) {
	tree := NewBinarySearchTree(nil)
	tree.Add("apple")

	as := tree.root.Val
	es := "apple"

	if as != es {
		t.Error("TestAdd(), actual:", as, " expected:", es)
	}
}

func TestAddSmaller(t *testing.T) {
	tree := NewBinarySearchTree(nil)
	tree.Add("m")
	tree.Add("a")

	ai := tree.root.Val
	ei := "m"
	if ai != ei {
		t.Error("TestAddSmaller(), actual:", ai, " expected:", ei)
	}

	ai = tree.root.left.Val
	ei = "a"
	if ai != ei {
		t.Error("TestAddSmaller(), actual:", ai, " expected:", ei)
	}
}

func TestAddLarger(t *testing.T) {
	tree := NewBinarySearchTree(nil)
	tree.Add("m")
	tree.Add("z")

	ai := tree.root.Val
	ei := "m"
	if ai != ei {
		t.Error("TestAddLarger(), actual:", ai, " expected:", ei)
	}

	ai = tree.root.right.Val
	ei = "z"
	if ai != ei {
		t.Error("TestAddLarger(), actual:", ai, " expected:", ei)
	}
}

func TestContains(t *testing.T) {
	tree := NewBinarySearchTree(nil)
	tree.Add("m")
	ab := tree.Contains("m")
	eb := true
	if ab != eb {
		t.Error("TestContains(), actual:", ab, " expected:", eb)
	}
}

func TestContainsEmpty(t *testing.T) {
	tree := NewBinarySearchTree(nil)
	ab := tree.Contains("m")
	eb := false
	if ab != eb {
		t.Error("TestContainsEmpty(), actual:", ab, " expected:", eb)
	}
}

func TestContainsNotFound(t *testing.T) {
	tree := NewBinarySearchTree(nil)
	tree.Add("m")
	ab := tree.Contains("z")
	eb := false
	if ab != eb {
		t.Error("TestContainsEmpty(), actual:", ab, " expected:", eb)
	}
}

func TestComparisonFuncDefault(t *testing.T) {
	tree := NewBinarySearchTree(nil)
	tree.Add("1")
	tree.Add("11")
	tree.Add("111")
	tree.Add("2")
	tree.Add("22")
	tree.Add("222")
	tree.Add("3")
	tree.Add("33")
	tree.Add("333")

	var expected []interface{}
	expected = append(expected, "1", "11", "111", "2", "22", "222", "3", "33", "333")

	actual := tree.ReturnAsArr(TraversalOrderIn)

	if !reflect.DeepEqual(expected, actual) {
		t.Error("TestComparisonFuncDefault(), actual:", actual, " expected:", expected)
	}
}

func _compare(val1 interface{}, val2 interface{}, CS int) bool {

	// convert the un-typed interface (which is storing string) to int
	// @TODO is this the best way?
	var v1 int
	var v2 int
	v1, _ = strconv.Atoi(val1.(string))
	v2, _ = strconv.Atoi(val2.(string))

	if CS == ComparisonSignEqual {
		return v1 == v2
	} else if CS == ComparisonSignLess {
		return v1 < v2
	} else if CS == ComparisonSignGreater {
		return v1 > v2
	} else {
		return false
	}

}

func TestComparisonFuncUserDef(t *testing.T) {

	tree := NewBinarySearchTree(_compare)
	tree.Add("1")
	tree.Add("11")
	tree.Add("111")
	tree.Add("2")
	tree.Add("22")
	tree.Add("222")
	tree.Add("3")
	tree.Add("33")
	tree.Add("333")

	expected := []int{1, 2, 3, 11, 22, 33, 111, 222, 333}

	actual := tree.ReturnAsArr(TraversalOrderIn)

	actualAsInt := make([]int, len(actual))
	for i := range actual {
		actualAsInt[i], _ = strconv.Atoi(actual[i].(string))
	}

	if !reflect.DeepEqual(expected, actualAsInt) {
		t.Error("TestComparisonFuncDefault(), actual:", actualAsInt, " expected:", expected)
	}
}

func TestAddXRandom(t *testing.T) {

	// @todo convert this method to Hashmap

	// list of unique ints
	vals := []int{}

	tree := NewBinarySearchTree(_compare)
	for j := 0; j < 50; j++ {

		// generate a uniq int
		var x int
		for true {
			x = rand.Intn(200)

			// make sure it's not in list
			found := false
			for k := 0; k < len(vals); k++ {
				if vals[k] == x {
					found = true
					break
				}
			}
			if !found {
				break
			}
		}

		vals = append(vals, x)
		tree.Add(strconv.Itoa(x))
	}

	sort.Ints(vals)

	actual := tree.ReturnAsArr(TraversalOrderIn)

	actualAsInt := make([]int, len(actual))
	for i := range actual {
		actualAsInt[i], _ = strconv.Atoi(actual[i].(string))
	}

	if !reflect.DeepEqual(vals, actualAsInt) {
		t.Error("TestComparisonFuncDefault(), actual:", actualAsInt, " expected:", vals)
	}
}
