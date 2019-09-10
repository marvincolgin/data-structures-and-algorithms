package linklist

import (
	"fmt"
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
	if list.Count() != 0 {
		t.Error("list != 0, actual:", list.Count())
	}
}

func TestAppend(t *testing.T) {
	list := LinkList{}
	list.Insert('1')

	if list.head == nil {
		t.Error("list.head is nil")
	}

	if list.Count() != 1 {
		t.Error("list.count() != 1, actual:", list.Count())
	}
}

func TestAppendMany(t *testing.T) {
	list := LinkList{}
	list.Append("0")
	list.Append("1")
	list.Append("2")
	list.Append("3")
	list.Append("4")
	list.Append("5")
	list.Append("6")
	list.Append("7")
	list.Append("8")
	list.Append("9")

	if list.Count() != 10 {
		t.Error("list.count()!=10, actual:", list.Count())
	}

	if list.head.value != "0" {
		t.Error("value!=0, actual:", list.head.value)
	}
	if list.head.next.value != "1" {
		t.Error("value!=1, actual:", list.head.next.value)
	}
	if list.head.next.next.value != "2" {
		t.Error("value!=2, actual:", list.head.next.next.value)
	}
	if list.head.next.next.next.value != "3" {
		t.Error("value!=3, actual:", list.head.next.next.next.value)
	}
	if list.head.next.next.next.next.value != "4" {
		t.Error("value!=4, actual:", list.head.next.next.next.next.value)
	}
	if list.head.next.next.next.next.next.value != "5" {
		t.Error("value!=5, actual:", list.head.next.next.next.next.next.value)
	}
	if list.head.next.next.next.next.next.next.value != "6" {
		t.Error("value!=6, actual:", list.head.next.next.next.next.next.next.value)
	}
	if list.head.next.next.next.next.next.next.next.value != "7" {
		t.Error("value!=7, actual:", list.head.next.next.next.next.next.next.next.value)
	}
	if list.head.next.next.next.next.next.next.next.next.value != "8" {
		t.Error("value!=8, actual:", list.head.next.next.next.next.next.next.next.next.value)
	}
	if list.head.next.next.next.next.next.next.next.next.next.value != "9" {
		t.Error("value!=9, actual:", list.head.next.next.next.next.next.next.next.next.next.value)
	}

}

func TestInsertOne(t *testing.T) {
	list := LinkList{}
	list.Insert("1")

	if list.head == nil {
		t.Error("list.head is nil")
	}

	if list.Count() != 1 {
		t.Error("list.count() != 1, actual:", list.Count())
	}

	if list.head.value != "1" {
		t.Error("list.head.valye != 1, actual:", list.head.value)
	}
}

func HelperInsertMany() LinkList {
	list := LinkList{}
	list.Insert("0")
	list.Insert("1")
	list.Insert("2")
	list.Insert("3")
	list.Insert("4")
	list.Insert("5")
	list.Insert("6")
	list.Insert("7")
	list.Insert("8")
	list.Insert("9")
	return list
}

func TestInsertMany(t *testing.T) {

	list := HelperInsertMany()

	if list.Count() != 10 {
		t.Error("list.count()!=10, actual:", list.Count())
	}

	if list.head.value != "9" {
		t.Error("value!=0, actual:", list.head.value)
	}
	if list.head.next.value != "8" {
		t.Error("value!=8, actual:", list.head.next.value)
	}
	if list.head.next.next.value != "7" {
		t.Error("value!=7, actual:", list.head.next.next.value)
	}
	if list.head.next.next.next.value != "6" {
		t.Error("value!=6, actual:", list.head.next.next.next.value)
	}
	if list.head.next.next.next.next.value != "5" {
		t.Error("value!=5, actual:", list.head.next.next.next.next.value)
	}
	if list.head.next.next.next.next.next.value != "4" {
		t.Error("value!=4, actual:", list.head.next.next.next.next.next.value)
	}
	if list.head.next.next.next.next.next.next.value != "3" {
		t.Error("value!=3, actual:", list.head.next.next.next.next.next.next.value)
	}
	if list.head.next.next.next.next.next.next.next.value != "2" {
		t.Error("value!=2, actual:", list.head.next.next.next.next.next.next.next.value)
	}
	if list.head.next.next.next.next.next.next.next.next.value != "1" {
		t.Error("value!=1, actual:", list.head.next.next.next.next.next.next.next.next.value)
	}
	if list.head.next.next.next.next.next.next.next.next.next.value != "0" {
		t.Error("value!=0, actual:", list.head.next.next.next.next.next.next.next.next.next.value)
	}
}

func TestIncludes(t *testing.T) {
	list := HelperInsertMany()
	if !list.Includes("5") {
		t.Error(".Includes(\"5\") != true, actual:", list.Includes("5"))
	}
}

func TestIncludesNotFound(t *testing.T) {
	list := HelperInsertMany()
	if list.Includes("five") {
		t.Error(".Includes(\"five\")==true, actual:", list.Includes("five"))
	}
}

/*
def test_toJSON():
    # Dump the LinkList to JSON and compare to what it should be
    ll = LinkList()
    helper_insert_many(ll)
    actual = ll.toJSON()
    expected = """{ "head": { "value": "9", "next": { "value": "8", "next": { "value": "7", "next": { "value": "6", "next": { "value": "5", "next": { "value": "4", "next": { "value": "3", "next": { "value": "2", "next": { "value": "1", "next": { "value": "0", "next": null, "prev": null }, "prev": null }, "prev": null }, "prev": null }, "prev": null }, "prev": null }, "prev": null }, "prev": null }, "prev": null }, "prev": null } }"""
    print(actual)
    print(expected)
    assert expected == actual
*/

func TestRemove(t *testing.T) {
	list := HelperInsertMany()
	if list.Remove("5") != true {
		t.Error("Remove(\"5\") failed")
	}
	if list.Count() != 9 {
		t.Error("Count()!=9")
	}
}

func TestPeekHead(t *testing.T) {
	list := HelperInsertMany()
	retBool, retVal := list.PeekHead()
	if !retBool {
		t.Error("PeekHead() failed.")
	}
	if retVal != "9" {
		t.Error("PeekHead() did not return \"9\"")
	}
}

func TestPeekHeadEmpty(t *testing.T) {
	list := LinkList{}
	retBool, _ := list.PeekHead()
	if retBool {
		t.Error("PeekHead() should not return TRUE.")
	}
}

func HelperInsertBefore() LinkList {
	list := LinkList{}
	list.Insert("1")
	list.Insert("3")
	list.Insert("2")
	return list
}

func TestInsertBefore(t *testing.T) {
	var list LinkList
	var expected, actual string

	list = HelperInsertBefore()
	list.InsertBefore("3", "4", false)
	expected = "2,4,3,1"
	actual = list.toStr()
	if expected != actual {
		t.Error("InsertBefore(), expected:", expected, " actual:", actual)
	}

	list = HelperInsertBefore()
	list.InsertBefore("1", "5", false)
	expected = "2,3,5,1"
	actual = list.toStr()
	if expected != actual {
		t.Error("InsertBefore(), expected:", expected, " actual:", actual)
	}

	list = HelperInsertBefore()
	list.InsertBefore("2", "5", false)
	expected = "5,2,3,1"
	actual = list.toStr()
	if expected != actual {
		t.Error("InsertBefore(), expected:", expected, " actual:", actual)
	}

	list = HelperInsertBefore()
	actualBool := list.InsertBefore("4", "5", false)
	expectedBool := false
	if expectedBool != actualBool {
		t.Error("InsertBefore(), expectedBool:", expectedBool, " actualBool:", actualBool)
	}

}

func TestInsertAfter(t *testing.T) {
	var list LinkList
	var expected, actual string

	list = HelperInsertBefore()
	list.InsertAfter("3", "5")
	expected = "2,3,5,1"
	actual = list.toStr()
	if expected != actual {
		t.Error("InsertAfter(), expected:", expected, " actual:", actual)
	}

	list = HelperInsertBefore()
	list.InsertAfter("2", "5")
	expected = "2,5,3,1"
	actual = list.toStr()
	if expected != actual {
		t.Error("InsertAfter(), expected:", expected, " actual:", actual)
	}

	list = HelperInsertBefore()
	actualBool := list.InsertAfter("4", "5")
	expectedBool := false
	if expectedBool != actualBool {
		t.Error("InsertAfter(), expectedBool:", expectedBool, " actualBool:", actualBool)
	}
}

func HelperKthFromEnd() LinkList {
	list := LinkList{}
	list.Insert("2")
	list.Insert("8")
	list.Insert("3")
	list.Insert("1")
	return list
}

func TestKthFromEnd(t *testing.T) {
	list := HelperKthFromEnd()
	var actual, expected string
	var actualBool, expectedBool bool

	actual = fmt.Sprintf("%v", list.KthFromEnd(0))
	expected = "2"
	if expected != actual {
		t.Error("KthFromEnd(), expected:", expected, " actual:", actual)
	}

	// "Happy Path" where k is not at the end, but somewhere in the middle of the linked list
	actual = fmt.Sprintf("%v", list.KthFromEnd(2))
	expected = "3"
	if expected != actual {
		t.Error("KthFromEnd(), expected:", expected, " actual:", actual)
	}

	// # Where k and the length of the list are the same
	actualBool = list.KthFromEnd(5).(bool)
	expectedBool = false
	if expectedBool != actualBool {
		t.Error("KthFromEnd(), expectedBool:", expectedBool, " actualBool:", actualBool)
	}

	// # Where k is not a positive integer
	actualBool = list.KthFromEnd(-1).(bool)
	expectedBool = false
	if expectedBool != actualBool {
		t.Error("KthFromEnd(), expectedBool:", expectedBool, " actualBool:", actualBool)
	}
}

func TestKthFromEnd_OneLinkList(t *testing.T) {
	list := LinkList{}
	list.Insert("blah")

	// Where the linked list is of a size 1
	actual := list.KthFromEnd(0).(string)
	expected := "blah"
	if expected != actual {
		t.Error("KthFromEnd(), expected:", expected, " actual:", actual)
	}
}

/*
def test_kthFromEnd_Exception():
    ll = helper_kthFromEnd()

    # TEST: Where k is greater than the length of the linked list
    with pytest.raises(AssertionError):
        assert(ll.kthFromEnd(6))
*/

func TestLinkListMerge(t *testing.T) {

	// # @TODO: TEST: Merge two unequal
	// # @TODO: TEST: Merge one empty list
	// # @TODO: TEST: Merge two empty lists
	// # @TODO: TEST: Merge a list with just 1 item

	listA := LinkList{}
	listA.Insert("apple")
	listA.Insert("bannana")
	listA.Insert("orange")

	listB := LinkList{}
	listB.Insert("cheerios")
	listB.Insert("frosted flakes")
	listB.Insert("wheaties")

	listA.MergeList(listA, listB)

	// @TODO: Interesting, it's in a different order than in python
	// -- expected := "apple,cheerios,bannana,frosted flakes,orange,wheaties"
	expected := "orange,wheaties,bannana,frosted flakes,apple,cheerios"
	actual := listA.toStr()

	if expected != actual {
		listA.MergeList(listA, listB)
		t.Error("MergeList(), expected:", expected, " actual:", actual)
	}
}
