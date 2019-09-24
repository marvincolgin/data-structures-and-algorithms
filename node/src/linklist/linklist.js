// LinkNode this is the internal object for individual link-nodes
module.exports = class LinkNode {

	constructor(value) {
		this.value = value;
		this.next = null;
		this.prev = null;
	 }

}

// LinkList is the internal data-structure
module.exports = class LinkList {

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


}

