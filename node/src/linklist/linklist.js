// LinkNode this is the internal object for individual link-nodes
class LinkNode {

	constructor(value) {
		this.value = value;
		this.next = null;
		this.prev = null;
	 }

}

// LinkList is the internal data-structure
class LinkList {

	constructor() {
		this.head = null;
      this.comparison_func = null;
	}

   // toStr dump list tos string
   // @retval string
   toStr() {
      // # c,cnt are limiters to make sure we don't go run away
      // # yes, we need cnt=self.count() and not -1, as we walk off list
      let c = 0
      let cnt = this.count()
      let buf = ""
      let ptr = this.head

      while (ptr != null) {
         let s = ptr.value  // @TODO type conversion?

         buf = buf + s + ","
         ptr = ptr.next
         c++
         if (c > cnt) {
            console.log("WAIT!!! Forever Loop!\nRecursive LinkList/Node\nbuf:[{buf}]")
            process.exit(1)
         }
      }

      if (buf.endsWith(',')) {
         buf = buf.substring(0,buf.length-1)
      }

      return buf
   }

   // Count the number of items
   // @retval int
   count() {
   	let cur = this.head

   	let c = 0
   	while (cur != null) {
		   c++
		   cur = cur.next
	   }

	   return c
   }

   // Peek a value from the front of the list
   // @retval obj{retBool:false, retVal:null}
   peek() {
      let retObj = {
         retBool: false,
         retVal : null
      }
      if (this.head != null) {
         retObj.retBool = true
         retObj.retVal = this.head.value
      }
      return retObj
   }

   // Append a value into LinkList
   // @retval bool
   append(value) {

      // Walk to end of list
      let prev = null;
      let cur = this.head;
      while (cur != null) {
         prev = cur
         cur = cur.next
      }

      // create the node and add it to the end
      let node = new LinkNode(value)

      if (prev == null) {
         this.head = node
      } else {
         prev.next = node
      }

      return true
   }

   // Insert a value into the link list
   // @retval bool
   insert(value) {
      let node = new LinkNode(value)
      node.next = this.head
      this.head = node
      return true
   }

   // Includes tests to see if a value exists
   // @retval bool
   includes(value) {
      let retVal = false

      let cur = this.head
      while (cur != null) {
         if (this.comparison_func != null) {
            if (this.comparison_func(cur.value, value)) {
               retVal = true
               break
            }
         } else {
            if (cur.value == value) {
               retVal = true
               break
            }
         }
         cur = cur.next
      }

      return retVal
   }

   // Remove a node from a list, given a specific value
   // @retval bool
   remove(value) {
      // BigO == O(n*2) ... I could eliminate self.includes(), but I think it's more readable
      // NOTE: only the first one found will be removed

      let retVal = false
      if (this.includes(value)) {
         let prev = null
         let cur = this.head

         while (cur != null) {

            let found = false
            if (this.comparison_func != null) {
            	if (this.comparison_func(cur.value, value))
            		found = True
            } else {
               if (cur.value == value) {
                  found = true
               }
            }

            if (found) {
               if (prev == null) {
                  this.head = cur.next
               } else {
                  prev.next = cur.next
               }
               retVal = true
               break
            }

            prev = cur
            cur = cur.next
         }

      }

      return retVal
   }

   // InsertBefore add a new node with the given newValue immediately BEFORE the node containg targetVal
   // @afterInsert: bool
   // @retval: bool
   insertBefore(targetVal, newVal, afterInstead=false)  {
      // # note: this bevahoir can be modified by the bool afterInstead
      // # BigO == O(n)

      // walk the list to find it or the end
      let found = false
      let prev = null
      let cur = this.head
      while (cur != null) {
         // @TODO convert to use comparison_func()
         if (cur.value == targetVal) {
            found = true
            break
         }
         prev = cur
         cur = cur.next
      }

      // # if found, put it in the chain, as a link right before the node containing value
      if (found) {
         let node = new LinkNode(newVal)
         if (afterInstead) {
            node.next = cur.next
            cur.next = node
         } else {
            node.next = cur
            if (prev == null) { // edge-case, if the targetVal is first node
               this.head = node
            } else {
               prev.next = node
            }
         }
      }

      return found
   }

   // InsertAfter add a new node with the given newValue immediately AFTER the node containg targetVal
   // @retval bool
   insertAfter(targetVal, newVal)  {
	   // BigO == O(n)
	   return this.insertBefore(targetVal, newVal, true)
   }

   // KthFromEnd finds the Kth element from the end of the list and returns value for node
   // @param k integer
   // @retval retObj{}
   kthFromEnd(k) {
      // BigO == O(n)

      // Only positive integers
      if (k < 0) {
         return {
            retBool: false,
            retVal: null
         }
      }

      let ptrA = this.head
      let ptrB = this.head

      // Walk ptrA out to "K" elements
      let tooSmall = false
      let c = 0
      while (c < k-1) {
         if (ptrA.next == null) {
            tooSmall = true
            break
         }
         ptrA = ptrA.next
         c = c + 1
      }
      if (tooSmall) {
         return {
            retBool: false,
            retVal: null
         }
      }

      // Walk ptrA and ptrB out to the end of the list
      // ptrB will point to our requested node
      // note: for short lengths where the value is found before k elements, we are going to skip walking
      // ptrB until the difference between it and ptrA is "k"
      while (ptrA.next != null) {
         ptrA = ptrA.next
         if (c >= k) {
            ptrB = ptrB.next
         }
         c = c + 1
      }

      return {
         retBool: true,
         retVal: ptrB.value
      }
   }

   // MergeList two lists together (zipper)
   // @param listA: LinkList
   // @param listB: LinkList
   // @retval LinkList
   mergeList(listA, listB) {
      // BigO == O(n)

      let ptrA = listA.head
      let ptrB = listB.head

      let prev = null
      while ( (ptrA != null) || (ptrB != null) ) {
         if (ptrA != null) {
            prev = ptrA
            ptrA = ptrA.next
            prev.next = ptrB
         }
         if (ptrB != null) {
            prev = ptrB
            ptrB = ptrB.next
            prev.next = ptrA
         }
      }

      return listA
   }


}

module.exports.LinkNode = LinkNode
module.exports.LinkList = LinkList
