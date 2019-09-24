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

      let cur = list.head
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
                  list.head = cur.next
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


}

module.exports.LinkNode = LinkNode
module.exports.LinkList = LinkList
