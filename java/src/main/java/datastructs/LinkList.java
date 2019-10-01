package datastructs;

import java.util.function.BiFunction;
import java.util.function.Consumer;

// @TODO use Vector for Node.value
// @TODO use comparisonFunc() and make tests for Vector

public class LinkList {

   public class RetObj {
      public Boolean retBool;
      public String retVal;

      public RetObj(Boolean b, String v) {
         this.retBool = b;
         this.retVal = v;
      }
   }

   public Node head;

   private BiFunction<String, String, Boolean> comparisonFunc;
   public void setComparisonFunc(BiFunction f) {
      this.comparisonFunc = f;
   }

   public LinkList(BiFunction cf) {
      this.head = null;
      this.comparisonFunc = cf;
   }

   class Node {
      public String value;
      public Node next;

      public Node(String v) {
         this.value = v;
         this.next = null;
      }
   }

   public void insert(String value) {
      Node node = new Node(value);
      node.next = this.head;
      this.head = node;
   }

   public int count() {
      int cnt = 0;
      Node cur = this.head;
      while (cur != null) {
         cnt += 1;
         cur = cur.next;
      }
      return cnt;
   }

   public Boolean includes(String value) {
      Boolean retval = false;
      Node cur = this.head;

      while (cur != null) {
         if (this.comparisonFunc != null) {
            if (this.comparisonFunc.apply(cur.value, value)) {
               retval = true;
               break;
            }
         }
         else {
            if (cur.value.compareTo(value) == 0) {
               retval = true;
               break;
            }
         }
         cur = cur.next;
      }

      return retval;
   }

   public RetObj peek() {
      RetObj retobj = new RetObj(false, null);

      if (this.head != null) {
         retobj.retBool = true;
         retobj.retVal = this.head.value;
      }

      return retobj;
   }

   public String toStr() {
      int c = 0;
      int cnt = this.count();

      String buf = new String("");
      Node cur = this.head;
      while (cur != null) {
         buf = buf + cur.value + ",";
         c += 1;
         cur = cur.next;
         if (c > cnt) {
            throw new RuntimeException("c > cnt");
         }
      }

      if (buf.endsWith(",")) {
         buf = buf.substring(0, buf.length()-1);
      }

      return buf;
   }

   public Boolean append(String value) {
      Node prev = null;
      Node cur = this.head;

      // walk to end of list
      while (cur != null) {
         prev = cur;
         cur = cur.next;
      }

      // create the node and add it to the end
      Node node = new Node(value);
      if (prev == null) {
         this.head = node;
      } else {
         prev.next = node;
      }

      return true;
   }

   public Boolean remove(String value) {
      // removes a node from a list, given a specific value
      // BigO == O(n*2) ... I could eliminate self.includes(), but I think it's more readable
      // NOTE: only the first one found will be removed

      Boolean retval = false;
      if (this.includes(value)) {

         Node prev = null;
         Node cur = this.head;

         while (cur != null) {

            Boolean found = false;
            if (this.comparisonFunc != null) {
               if (this.comparisonFunc.apply(cur.value, value)) {
                  found = true;
               }
            }
            else
            if (cur.value.compareTo(value)==0) {
               found = true;
            }

            if (found) {
               if (prev == null) {
                  this.head = cur.next;
               } else {
                  prev.next = cur.next;
               }
               retval = true;
               break;
            }

            prev = cur;
            cur = cur.next;
         }
      }

      return retval;
   }

   public String get(String value) {
      // traverse list and determine if a value exist

      Node cur = this.head;
      while (cur != null) {
         if (this.comparisonFunc != null) {
            if (this.comparisonFunc.apply(cur.value, value)) {
               return cur.value;
            }
         }
         else
         if (cur.value.compareTo(value)==0) {
            return cur.value;
         }
         cur = cur.next;
      }
      throw new RuntimeException("Not Found, but it has to be found.");
   }

   private Boolean insertBeforeOrAfter(String targetVal, String newVal, Boolean afterInstead) {
      // add a new node with the given newValue immediately BEFORE the node containg targetVal
      // note: this bevahoir can be modified by the bool afterInstead
      // BigO == O(n)

      // walk the list to find it or the end
      Boolean found = false;
      Node prev = null;
      Node cur = this.head;

      while (cur != null) {
         if (cur.value.compareTo(targetVal)==0) {
            found = true;
            break;
         }
         prev = cur;
         cur = cur.next;
      }

      // if found, put it in the chain, as a link right before the node containing value
      if (found) {
         Node node = new Node(newVal);
         if (afterInstead) {
            node.next = cur.next;
            cur.next = node;
         } else {
            node.next = cur;
            if (prev == null) { // edge-case, if the targetVal is first node
               this.head = node;

            } else {
               prev.next = node;
            }
         }
      }

      return found;
   }
   public Boolean insertBefore(String targetVal, String newVal) {
      return this.insertBeforeOrAfter(targetVal, newVal, false);
   }
   public Boolean insertAfter(String targetVal, String newVal) {
      // add a new node with the given newValue immediately AFTER the node containg targetVal
      // BigO == O(n)
      return this.insertBeforeOrAfter(targetVal, newVal, true);
   }
   public void traverse(Consumer actionFunc) {
      // traverse the linklist and call the action_func with the value
      Node cur = this.head;
      while (cur != null) {
         actionFunc.accept(cur.value);
         cur = cur.next;
      }
   }
}
/*
    def traverse(self, action_func):
        cur = self.head
        while cur:
            action_func(cur.value)
            cur = cur.next

    def kthFromEnd(self, k):
        # finds the Kth element from the end of the list and returns value for node
        # BigO == O(n)

        # Only positive integers
        if k < 0:
            raise AssertionError(f'WAIT!!! You must pass a positive integer, k:[{k}]')

        ptrA = self.head
        ptrB = self.head

        # Walk ptrA out to "K" elements
        tooSmall = False
        c = 0
        while c < k-1:
            if ptrA.next is None:
                tooSmall = True
                break
            ptrA = ptrA.next
            c += 1
        if tooSmall:
            raise AssertionError(f'WAIT!!! There are not enough elements in the link list for k:[{k}].')

        # Walk ptrA and ptrB out to the end of the list
        # ptrB will point to our requested node
        # note: for short lengths where the value is found before k elements, we are going to skip walking
        # ptrB until the difference between it and ptrA is "k"
        while ptrA.next is not None:
            ptrA = ptrA.next
            if c >= k:
                ptrB = ptrB.next
            c += 1

        return ptrB.value


    def mergeList(self, listA, listB):
        # Merge two lists
        # BigO == O(n)

        ptrA = listA.head
        ptrB = listB.head

        while ptrA is not None or ptrB is not None:
            if ptrA is not None:
                prev = ptrA
                ptrA = ptrA.next
                prev.next = ptrB
            if ptrB is not None:
                prev = ptrB
                ptrB = ptrB.next
                prev.next = ptrA

        return listA


if __name__ == "__main__":

    listA = LinkList()
    listA.append('apple')
    listA.append('bannana')
    listA.append('orange')

    listB = LinkList()
    listB.append('cheerios')
    listB.append('frosted flakes')
    listB.append('wheaties')

    expected = 'apple,cheerios,bannan,frosted flakes,orange,wheaties'
    listA.mergeList(listA, listB)
    actual = listA.toStr()

    print(f'actual:[{actual}]')


    def toJSON(self):
        # dump object to JSON and return as String
        buf = json.dumps(self, default=lambda o: o.__dict__, indent=0, separators=(',', ': '))
        buf = buf.replace('\n', ' ').replace('\r', '')
        return buf


*/