// LinkNode this is the internal object for individual link-nodes
module.exports = class LinkNode {
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

}
