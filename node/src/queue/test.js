var chai = require('chai');
var expect = chai.expect; // we are using the 'expect' style of Chai

var Queue = require('./queue').Queue


function HelperEnqueueLots() {
   q = new Queue()
   q.enqueue('pao de queijo')
   q.enqueue('pappa sandwidh')
   q.enqueue('banana')
   q.enqueue('crackers')
   q.enqueue('strawberries')
   q.enqueue('chocolate chips')
   return q
}

describe('new Queue()', function() {
   it('new Queue()', function() {
      expect(new Queue()).to.be.an.instanceof(Queue);
   })

   it ('Queue.enqueue()', function() {
      q = new Queue()
      q.enqueue('pao de queijo')
      expect(q.count()).to.be.equal(1)
   })

   it('Queue.enqueue()::LOTS', function() {
      q = HelperEnqueueLots()
      expect(q.count()).to.be.equal(6)
   })

   it('Queue.dequeue()::SUCCESS', function() {
      q = HelperEnqueueLots()
      expect(q.dequeue('banana')).to.be.true
      expect(q.count()).to.be.equal(5)
   })

   it('Queue.dequeue()::ERROR', function() {
      q = HelperEnqueueLots()
      expect(q.dequeue('somethingyouwillnotfind')).to.be.false
      expect(q.count()).to.be.equal(6)
   })

   it('Queue.peek()', function() {
      q = HelperEnqueueLots()
      retObj = q.peek()
      expect(retObj.retBool).to.be.true
      expect(retObj.retVal).to.be.equal('pao de queijo')
   })

   it('Queue.peek()::EMPTY', function() {
      q = new Queue()
      retObj = q.peek()
      expect(retObj.retBool).to.be.false
      expect(retObj.retVal).to.be.null
   })

   it('Queue.dequeue()::UNTIL EMPTY', function() {
      q = HelperEnqueueLots()
      arr = q.toStr().split(',')
      for (var x in arr) {
         q.dequeue(arr[x])
      }
      expect(q.count()).to.be.equal(0)
   })
})
