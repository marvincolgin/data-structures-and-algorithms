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

}

module.exports.LinkNode = LinkNode
module.exports.LinkList = LinkList
