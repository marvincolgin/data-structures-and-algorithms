package datastructs;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

import java.beans.Transient;

import datastructs.LinkList;


public class LinkListTest {

   public LinkList helperInsertMany() {
      LinkList ll = new LinkList(null);
      ll.insert("0");
      ll.insert("1");
      ll.insert("2");
      ll.insert("3");
      ll.insert("4");
      ll.insert("5");
      ll.insert("6");
      ll.insert("7");
      ll.insert("8");
      ll.insert("9");
      return ll;
   }

   @Test
   public void testLinkListEmpty() {
      LinkList ll = new LinkList(null);
      assertNull(ll.head, "list.head==null");
   }
   @Test
   public void testInsert() {
      String val = new String("50");
      assertTrue(val.compareTo("50")==0);
      LinkList ll = new LinkList(null);
      ll.insert(val);
   }
   @Test
   public void testCount() {
      LinkList ll = this.helperInsertMany();
      Integer expected = 10;
      assertTrue(ll.count()==expected, "Count must match expected");
   }
   @Test
   public void testInsertMany() {
      LinkList ll = this.helperInsertMany();
      assertTrue(ll.head.value.compareTo("9")==0);
      assertTrue(ll.head.next.value.compareTo("8")==0);
      assertTrue(ll.head.next.next.value.compareTo("7")==0);
      assertTrue(ll.head.next.next.next.value.compareTo("6")==0);
      assertTrue(ll.head.next.next.next.next.value.compareTo("5")==0);
      assertTrue(ll.head.next.next.next.next.next.value.compareTo("4")==0);
      assertTrue(ll.head.next.next.next.next.next.next.value.compareTo("3")==0);
      assertTrue(ll.head.next.next.next.next.next.next.next.value.compareTo("2")==0);
      assertTrue(ll.head.next.next.next.next.next.next.next.next.value.compareTo("1")==0);
      assertTrue(ll.head.next.next.next.next.next.next.next.next.next.value.compareTo("0")==0);
   }
   @Test
   public void testIncludes() {
      LinkList ll = this.helperInsertMany();
      assertTrue(ll.includes("5"));
   }
   @Test
   public void testIncludesNotFound() {
      LinkList ll = this.helperInsertMany();
      assertFalse(ll.includes("five"));
   }
   @Test
   public void testPeek() {
      LinkList ll = this.helperInsertMany();
      LinkList.RetObj retobj = ll.peek();
      assertTrue(retobj.retBool==true);
      assertTrue(retobj.retVal.compareTo("9")==0);
   }
   @Test
   public void testPeekEmpty() {
      LinkList ll = new LinkList(null);
      LinkList.RetObj retobj = ll.peek();
      assertTrue(retobj.retBool==false);
      assertTrue(retobj.retVal==null);
   }
   @Test
   public void testAppend() {
      LinkList ll = new LinkList(null);
      ll.insert("2");
      ll.insert("3");
      ll.insert("1");
      ll.append("5");
      String r = ll.toStr();
      assertTrue(r.compareTo("1,3,2,5")==0);
   }
   @Test
   public void testRemove() {
      LinkList ll = this.helperInsertMany();
      assertTrue(ll.remove("5")==true);
      assertTrue(ll.count()==9);
   }
}

/*

def test_remove():
    ll = LinkList()
    helper_insert_many(ll)
    actual = ll.remove('5')
    expected = True
    assert actual == expected
    assert ll.count() == 9


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
def test_toJSON():
    # Dump the LinkList to JSON and compare to what it should be
    ll = LinkList()
    helper_insert_many(ll)
    actual = ll.toJSON()
    expected = """{ "head": { "value": "9", "next": { "value": "8", "next": { "value": "7", "next": { "value": "6", "next": { "value": "5", "next": { "value": "4", "next": { "value": "3", "next": { "value": "2", "next": { "value": "1", "next": { "value": "0", "next": null, "prev": null }, "prev": null }, "prev": null }, "prev": null }, "prev": null }, "prev": null }, "prev": null }, "prev": null }, "prev": null }, "prev": null }, "comparison_func": null }"""
    print(actual)
    print(expected)
    assert expected == actual



*/