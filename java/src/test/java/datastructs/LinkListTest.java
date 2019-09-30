package datastructs;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

import java.beans.Transient;

import datastructs.LinkList;


public class LinkListTest {
    @Test
    public void testLinkListEmpty() {
        LinkList ll = new LinkList(null);
        assertNull(ll.head, "list.head==null");
    }
}

/*
from link_list import LinkList, LinkNode
import pytest


def helper_insert_many(ll):
    ll.insert('0')
    ll.insert('1')
    ll.insert('2')
    ll.insert('3')
    ll.insert('4')
    ll.insert('5')
    ll.insert('6')
    ll.insert('7')
    ll.insert('8')
    ll.insert('9')


def test_class_exists():
    assert LinkList
    assert LinkNode


def test_count():
    ll = LinkList()
    helper_insert_many(ll)
    expected = 10
    actual = ll.count()
    assert actual == expected


def test_insert():
    ll = LinkList()
    ll.insert('one')
    assert ll.head.value == 'one'


def test_insert_many():
    ll = LinkList()
    helper_insert_many(ll)
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


def test_includes():
    ll = LinkList()
    helper_insert_many(ll)
    expected = True
    actual = ll.includes('5')
    assert expected == actual


def test_includes_notfound():
    ll = LinkList()
    helper_insert_many(ll)
    expected = False
    actual = ll.includes('five')
    assert expected == actual


def test_toJSON():
    # Dump the LinkList to JSON and compare to what it should be
    ll = LinkList()
    helper_insert_many(ll)
    actual = ll.toJSON()
    expected = """{ "head": { "value": "9", "next": { "value": "8", "next": { "value": "7", "next": { "value": "6", "next": { "value": "5", "next": { "value": "4", "next": { "value": "3", "next": { "value": "2", "next": { "value": "1", "next": { "value": "0", "next": null, "prev": null }, "prev": null }, "prev": null }, "prev": null }, "prev": null }, "prev": null }, "prev": null }, "prev": null }, "prev": null }, "prev": null }, "comparison_func": null }"""
    print(actual)
    print(expected)
    assert expected == actual


def test_append():
    ll = LinkList()
    ll.insert('2')
    ll.insert('3')
    ll.insert('1')
    ll.append('5')
    expected = '1,3,2,5'
    actual = ll.toStr()
    assert expected == actual

def test_remove():
    ll = LinkList()
    helper_insert_many(ll)
    actual = ll.remove('5')
    expected = True
    assert actual == expected
    assert ll.count() == 9


def test_peekHead():
    ll = LinkList()
    helper_insert_many(ll)
    expectedStr = "9"
    expectedBool = True
    actualBool,actualStr = ll.peekHead()
    assert expectedStr == actualStr
    assert expectedBool == actualBool


def test_peekHead_empty():
    ll = LinkList()
    expectedStr = ""
    expectedBool = False
    actualBool,actualStr = ll.peekHead()
    assert expectedBool == actualBool


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


def test_traverse():
    actual = []
    def visit(value):
        actual.append(value)
    ll = LinkList()
    helper_insert_many(ll)
    ll.traverse(visit)
    expected = ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
    assert actual == expected


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
    listA.append('apple')
    listA.append('bannana')
    listA.append('orange')

    listB = LinkList()
    listB.append('cheerios')
    listB.append('frosted flakes')
    listB.append('wheaties')

    listA.mergeList(listA, listB)

    expected = 'apple,cheerios,bannana,frosted flakes,orange,wheaties'
    actual = listA.toStr()

    assert expected == actual


*/