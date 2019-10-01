package datastructs;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

import java.beans.Transient;
import java.util.function.BiFunction;
import java.util.function.Consumer;
import java.util.concurrent.atomic.AtomicReference;
import java.util.function.BiConsumer;

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

   public LinkList helperInsertBefore() {
      LinkList ll = new LinkList(null);
      ll.insert("1");
      ll.insert("3");
      ll.insert("2");
      return ll;
   }

   public LinkList helperKthFromEnd() {
      LinkList ll = new LinkList(null);
      ll.insert("2");
      ll.insert("8");
      ll.insert("3");
      ll.insert("1");
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
   @Test
   public void testGet() {
      LinkList ll = this.helperInsertMany();
      String actual = ll.get("5");
      assertTrue(actual.compareTo(new String("5"))==0);
   }
   @Test
   public void testInsertBefore() {
      LinkList ll;
      String actual;

      ll = helperInsertBefore();
      ll.insertBefore(new String("3"), new String("4"));
      actual = ll.toStr();
      assertTrue(actual.compareTo("2,4,3,1")==0);
      ll = null;

      ll = helperInsertBefore();
      ll.insertBefore(new String("1"), new String("5"));
      actual = ll.toStr();
      assertTrue(actual.compareTo("2,3,5,1")==0);
      ll = null;

      ll = helperInsertBefore();
      ll.insertBefore(new String("2"), new String("5"));
      actual = ll.toStr();
      assertTrue(actual.compareTo("5,2,3,1")==0);
      ll = null;

      ll = helperInsertBefore();
      Boolean ab = ll.insertBefore(new String("4"), new String("5"));
      assertTrue(ab == false);
      ll = null;
   }
   @Test
   public void testInsertAfter() {
      LinkList ll;
      String actual;

      ll = helperInsertBefore();
      ll.insertAfter(new String("3"), new String("5"));
      actual = ll.toStr();
      assertTrue(actual.compareTo("2,3,5,1")==0);
      ll = null;

      ll = helperInsertBefore();
      ll.insertAfter(new String("2"), new String("5"));
      actual = ll.toStr();
      assertTrue(actual.compareTo("2,5,3,1")==0);
      ll = null;

      ll = helperInsertBefore();
      Boolean ab = ll.insertAfter(new String("4"), new String("5"));
      assertTrue(ab == false);
      ll = null;
   }

   private BiFunction<String, String, Boolean> _customCompare = (s1, s2) -> {
      Boolean retval = (s1.compareTo(s2)==0);
      return retval;
   };

   @Test
   public void testTraverse() {
      LinkList ll = this.helperInsertMany();

      String[] actual;
      actual = new String[ll.count()];

      AtomicReference<Integer> idx = new AtomicReference<>();
      idx.set(0);

      Consumer<String> _visit = (value) -> {
         actual[idx.get()] = value;
         idx.set(idx.get()+1);
      };

      ll.traverse(_visit);

      String[] expected = {"9", "8", "7", "6", "5", "4", "3", "2", "1", "0"};
      assertArrayEquals(actual, expected);
   }

   @Test
   void testKthFromEnd() {
      String actual;
      LinkList ll = helperKthFromEnd();

      actual = ll.kthFromEnd(0);
      assertTrue(actual.compareTo("2")==0);

      // "Happy Path" where k is not at the end, but somewhere in the middle of the linked list
      actual = ll.kthFromEnd(2);
      assertTrue(actual.compareTo("3")==0);

      // Where k and the length of the list are the same
      assertThrows(RuntimeException.class, () -> {
         ll.kthFromEnd(5);
      });

      // Where k is not a positive integer
      assertThrows(RuntimeException.class, () -> {
         ll.kthFromEnd(-1);
      });
   }

   @Test
   void testKthFromEndOneLinkList() {
      LinkList ll = new LinkList(null);
      ll.insert("blah");

      // Where the linked list is of a size 1
      String actual = ll.kthFromEnd(0);
      assertTrue(actual.compareTo("blah")==0);
   }

   @Test
   void testKthFromEndException() {
      String actual;
      LinkList ll = helperKthFromEnd();

      // Where k is not a positive integer
      assertThrows(RuntimeException.class, () -> {
         ll.kthFromEnd(6);
      });
   }

   @Test
   void testMerge() {
      // @TODO: TEST: Merge two unequal
      // @TODO: TEST: Merge one empty list
      // @TODO: TEST: Merge two empty lists
      // @TODO: TEST: Merge a list with just 1 item

      LinkList listA = new LinkList(null);
      listA.append("apple");
      listA.append("bannana");
      listA.append("orange");

      LinkList listB = new LinkList(null);
      listB.append("cheerios");
      listB.append("frosted flakes");
      listB.append("wheaties");

      listA.mergeList(listA, listB);

      String actual;
      actual = listA.toStr();

      assertTrue(actual.compareTo("apple,cheerios,bannana,frosted flakes,orange,wheaties")==0);
   }
}

/*
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