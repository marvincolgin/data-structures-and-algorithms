var LinkList = require('../linklist/linklist').LinkList


// Stack implementation of LIFO
class Stack {

   // Init inistantiate the class and internal LinkList
	constructor() {
      this._data = new LinkList();
   }

   // Count the number of items in linklist
   // @retval int
   count() {
      return this._data.count()
   }

   // Pop an item from the front of the stack
   // @retval retObj:{}
   pop() {
      let retObj = this._data.peek()
      if (retObj.retBool) {
         stack._data.remove(retObj.retVal)
      }
      return retObj
   }

   // Push an item to top of Stack
   // @param val
   // @retval bool
   push(val) {
      this._data.insert(val)
      return true
   }

   // Peek an item at top of Stack
   // @retval retObj
   peek() {
      return stack._data.peek()
   }


}

module.exports.Stack = Stack
