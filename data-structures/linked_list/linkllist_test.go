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

/*
def helper_insertBefore():
    ll = LinkList()
    ll.insert('1')
    ll.insert('3')
    ll.insert('2')
    return ll


def test_insertBefore():
    ll = helper_insertBefore()
    ll.insertBefore('3', '4')
    expected = '2,4,3,1'
    actual = ll.toStr()
    assert expected == actual

    ll = helper_insertBefore()
    ll.insertBefore('1', '5')
    expected = '2,3,5,1'
    actual = ll.toStr()
    assert expected == actual

    ll = helper_insertBefore()
    ll.insertBefore('2', '5')
    expected = '5,2,3,1'
    actual = ll.toStr()
    assert expected == actual

    ll = helper_insertBefore()
    actual = ll.insertBefore('4', '5')
    expected = False
    assert expected == actual
    # @TODO: Assignment wanted me to raise an exception
    # @ I've worked way too long on this, but this is how...
    # self.assertRaises(SomeCoolException, mymod.myfunc)


def test_insertAfter():
    ll = helper_insertBefore()
    ll.insertAfter('3', '5')
    expected = '2,3,5,1'
    actual = ll.toStr()
    assert expected == actual

    ll = helper_insertBefore()
    ll.insertAfter('2', '5')
    expected = '2,5,3,1'
    actual = ll.toStr()
    assert expected == actual

    ll = helper_insertBefore()
    actual = ll.insertAfter('4', '5')
    expected = False
    assert expected == actual
    # @TODO: Assignment wanted me to raise an exception
    # @ I've worked way too long on this, but this is how...
    # self.assertRaises(SomeCoolException, mymod.myfunc)


def helper_kthFromEnd():
    ll = LinkList()
    ll.insert("2")
    ll.insert("8")
    ll.insert("3")
    ll.insert("1")
    return ll


def test_kthFromEnd():
    ll = helper_kthFromEnd()
    print(ll.toStr())

    actual = ll.kthFromEnd(0)
    expected = "2"
    assert actual == expected

    # "Happy Path" where k is not at the end, but somewhere in the middle of the linked list
    actual = ll.kthFromEnd(2)
    expected = "3"
    assert actual == expected

    # Where k and the length of the list are the same
    with pytest.raises(AssertionError):
        assert(ll.kthFromEnd(5))

    # Where k is not a positive integer
    with pytest.raises(AssertionError):
        assert(ll.kthFromEnd(-1))


def test_kthFromEnd_OneLinkList():
    ll = LinkList()
    ll.insert("blah")

    #Where the linked list is of a size 1
    actual = ll.kthFromEnd(0)
    expected = "blah"
    assert actual == expected


def test_kthFromEnd_Exception():
    ll = helper_kthFromEnd()

    # TEST: Where k is greater than the length of the linked list
    with pytest.raises(AssertionError):
        assert(ll.kthFromEnd(6))


def test_ll_merge():

    # @TODO: TEST: Merge two unequal
    # @TODO: TEST: Merge one empty list
    # @TODO: TEST: Merge two empty lists
    # @TODO: TEST: Merge a list with just 1 item

    listA = LinkList()
    listA.Insert('apple')
    listA.Insert('bannana')
    listA.Insert('orange')

    listB = LinkList()
    listB.Insert('cheerios')
    listB.Insert('frosted flakes')
    listB.Insert('wheaties')

    listA.mergeList(listA, listB)

    expected = 'apple,cheerios,bannana,frosted flakes,orange,wheaties'
    actual = listA.toStr()

    assert expected == actual

*/
