var LinkList = require('../linklist/linklist').LinkList


// Stack implementation of LIFO
class Queue {

   constructor() {
      this._data = new LinkList()
   }

   // @retval int
   count() {
      return this._data.count()
   }

   // @retval string
   toStr() {
      return this._data.toStr()
   }

   // @retval bool
   enqueue(val) {
      // Add a value to the queue
      return this._data.append(val)
   }

   // @retval bool
   dequeue(val){
      // Remove entry from queue with a given value
      // NOTE: will only remove the first element found with val
      return this._data.remove(val)
   }

   // @retval retObj:{}
   peek() {
      // Get value from the head of the queue (without removing it)
      return this._data.peek()
   }
}

module.exports.Queue = Queue
