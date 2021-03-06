var chai = require('chai');
var expect = chai.expect; // we are using the 'expect' style of Chai

var Stack = require('./stack').Stack


function HelperStackAddLots() {
	stack = new Stack()
	stack.push("pao de queijo")
	stack.push("pappa sandwich")
	stack.push("banana")
	return stack
}

describe('new Stack()', function() {
   it('new stack()', function() {
      expect(new Stack()).to.be.an.instanceof(Stack);
   })

   it('push() && peek()', function() {
      stack = new Stack()
      expect(stack.push('pao de queijo')).to.be.true
   })

   it('count()', function() {
      stack = HelperStackAddLots()
      expect(stack.count()).to.be.equal(3)
   })

   it('pop()', function() {
      stack = HelperStackAddLots()
      retObj = stack.pop()
      expect(retObj.retBool).to.be.true
      expect(retObj.retVal).to.be.equal('banana')
      expect(stack.count()==2)
   })

   it('pop()::until Empty', function() {
      stack = HelperStackAddLots()

      var i, len=stack.count()
      for (i=0; i<len; i++) {
         let retObj = stack.pop()

         let expectedBool = true
         let expectedVal = ''
         if (i == 0) {
            expectedVal = "banana"
         }
         else
         if (i == 1) {
            expectedVal = "pappa sandwich"
         }
         else
         if (i == 2) {
            expectedVal = "pao de queijo"
         } else {
            console.log('ERROR!!! TestPop(), we should never be here i:', i,  'len:', len)
         }
         expect(retObj.retBool).to.be.equal(expectedBool)
         expect(retObj.retVal).to.be.equal(expectedVal)
      }

      // Make sure it's reporting 0 for count
      len = stack.count()
      expect(stack.count()).to.be.equal(0)

      // Pop one more to test error
      let expObj = {retBool: false, retVal: null}
      let retObj = stack.pop()
      expect(retObj.retBool).to.be.equal(expObj.retBool)
      expect(retObj.retVal).to.be.equal(expObj.retVal)
   })
})
