var chai = require('chai');
var expect = chai.expect; // we are using the 'expect' style of Chai

var LinkNode = require('./linklist').LinkNode
var LinkList = require('./linklist').LinkList


function HelperInsertMany() {
	list = new LinkList()
	list.insert('0')
	list.insert('1')
	list.insert('2')
	list.insert('3')
	list.insert('4')
	list.insert('5')
	list.insert('6')
	list.insert('7')
	list.insert('8')
	list.insert('9')
	return (list)
}


function HelperInsertBefore() {
	list = new LinkList()
	list.insert('1')
	list.insert('3')
	list.insert('2')
	return list
}

function HelperKthFromEnd() {
	list = new LinkList()
	list.insert('2')
	list.insert('8')
	list.insert('3')
	list.insert('1')
	return (list)
}

describe('new linknode()', function() {
   it('Can Create', function() {
      expect(new LinkNode()).to.be.an.instanceof(LinkNode);
  });
});

describe('new linklist()', function() {
   it('Can Create', function() {
      expect(new LinkList()).to.be.an.instanceof(LinkList);
   })

   it('count()==0', function() {
      expect(new LinkList().count()).to.be.equal(0)
   })

   it('peek()', function() {
      list = HelperInsertMany()
      retObj = list.peek()

      expect(retObj.retBool).to.be.true
      expect(retObj.retVal).to.be.equal('9')
   })

   it('peek()::empty', function() {
      list = new LinkList()
      retObj = list.peek()

      expect(retObj.retBool).to.be.false
      expect(retObj.retVal).to.be.null
   })

   it('append()', function () {
      linklist = new LinkList()
      linklist.append('1')
      expect(linklist.head).to.not.be.null

      expect(linklist.count()).to.be.equal(1)
   })

   it('append()::many', function () {
      list = new LinkList()
      list.append('0')
      list.append('1')
      list.append('2')
      list.append('3')
      list.append('4')
      list.append('5')
      list.append('6')
      list.append('7')
      list.append('8')
      list.append('9')

      expect(list.count()).to.be.equal(10)
      expect(list.head.value).to.be.equal('0')
      expect(list.head.next.value).to.be.equal('1')
      expect(list.head.next.next.value).to.be.equal('2')
      expect(list.head.next.next.next.value).to.be.equal('3')
      expect(list.head.next.next.next.next.value).to.be.equal('4')
      expect(list.head.next.next.next.next.next.value).to.be.equal('5')
      expect(list.head.next.next.next.next.next.next.value).to.be.equal('6')
      expect(list.head.next.next.next.next.next.next.next.value).to.be.equal('7')
      expect(list.head.next.next.next.next.next.next.next.next.value).to.be.equal('8')
      expect(list.head.next.next.next.next.next.next.next.next.next.value).to.be.equal('9')
   })

   it('insert()', function () {
      list = new LinkList()
      list.insert('1')

      expect(list.head).to.not.be.null
      expect(list.count()).to.be.equal(1)
      expect(list.head.value).to.be.equal('1')
   })

   it ('insert()::many', function () {
      list = HelperInsertMany()

      expect(list.count()).to.be.equal(10)

      expect(list.head.value).to.be.equal('9')
      expect(list.head.next.value).to.be.equal('8')
      expect(list.head.next.next.value).to.be.equal('7')
      expect(list.head.next.next.next.value).to.be.equal('6')
      expect(list.head.next.next.next.next.value).to.be.equal('5')
      expect(list.head.next.next.next.next.next.value).to.be.equal('4')
      expect(list.head.next.next.next.next.next.next.value).to.be.equal('3')
      expect(list.head.next.next.next.next.next.next.next.value).to.be.equal('2')
      expect(list.head.next.next.next.next.next.next.next.next.value).to.be.equal('1')
      expect(list.head.next.next.next.next.next.next.next.next.next.value).to.be.equal('0')
   })

   it ('toStr()::many', function() {
      list = HelperInsertMany()

      expect(list.toStr()).to.be.equal('9,8,7,6,5,4,3,2,1,0')
   })

   it ('includes()==true', function() {
      list = HelperInsertMany()
      expect(list.includes('5')).to.be.true
   })

   it ('includes()==false', function() {
      list = HelperInsertMany()
      expect(list.includes('five')).to.be.false
   })

   it ('remove()', function () {
      list = HelperInsertMany()
      expect(list.remove('5')).to.be.true
      expect(list.count()).to.be.equal(9)
   })

   it ('insertBefore()', function() {
      list = HelperInsertBefore()
      list.insertBefore('3', '4', false)
      expect(list.toStr()).to.be.equal('2,4,3,1')

      list = HelperInsertBefore()
      list.insertBefore('1', '5', false)
      expect(list.toStr()).to.be.equal('2,3,5,1')

      list = HelperInsertBefore()
      list.insertBefore('2', '5', false)
      expect(list.toStr()).to.be.equal('5,2,3,1')

      list = HelperInsertBefore()
      expect(list.insertBefore('4', '5', false)).to.be.false

   })

   it ('insertAfter()', function() {
      list = HelperInsertBefore()
      list.insertAfter('3', '5')
      expect(list.toStr()).to.be.equal('2,3,5,1')

      list = HelperInsertBefore()
      list.insertAfter('2', '5')
      expect(list.toStr()).to.be.equal('2,5,3,1')

      list = HelperInsertBefore()
      expect(list.insertAfter('4', '5')).to.be.false
   })

   it ('kthFromEnd()', function() {
      list = HelperKthFromEnd()

      retObj = list.kthFromEnd(0)
      expect(retObj.retBool).to.be.true
      expect(retObj.retVal).to.be.equal('2')

      // 'Happy Path' where k is not at the end, but somewhere in the middle of the linked list
      retObj = list.kthFromEnd(2)
      expect(retObj.retBool).to.be.true
      expect(retObj.retVal).to.be.equal('3')

      // # Where k and the length of the list are the same
      retObj = list.kthFromEnd(5)
      expect(retObj.retBool).to.be.false

      // # Where k is not a positive integer
      retObj = list.kthFromEnd(-1)
      expect(retObj.retBool).to.be.false

   })

   it ('kthFromEnd()::OneValueInLinkList', function() {
      list = new LinkList()
      list.insert('blah')

      // Where the linked list is of a size 1
      retObj = list.kthFromEnd(0)
      expect(retObj.retBool).to.be.true
      expect(retObj.retVal).to.be.equal('blah')
   })


   it ('listMerge()', function() {

      // # @TODO: TEST: Merge two unequal
      // # @TODO: TEST: Merge one empty list
      // # @TODO: TEST: Merge two empty lists
      // # @TODO: TEST: Merge a list with just 1 item

      listA = new LinkList()
      listA.insert('apple')
      listA.insert('bannana')
      listA.insert('orange')

      listB = new LinkList()
      listB.insert('cheerios')
      listB.insert('frosted flakes')
      listB.insert('wheaties')

      listA.mergeList(listA, listB)

      expect(listA.toStr()).to.be.equal('orange,wheaties,bannana,frosted flakes,apple,cheerios')
   })

})



/*
def test_toJSON():
    # Dump the LinkList to JSON and compare to what it should be
    ll = LinkList()
    helper_insert_many(ll)
    actual = ll.toJSON()
    expected = '''{ 'head': { 'value': '9', 'next': { 'value': '8', 'next': { 'value': '7', 'next': { 'value': '6', 'next': { 'value': '5', 'next': { 'value': '4', 'next': { 'value': '3', 'next': { 'value': '2', 'next': { 'value': '1', 'next': { 'value': '0', 'next': null, 'prev': null }, 'prev': null }, 'prev': null }, 'prev': null }, 'prev': null }, 'prev': null }, 'prev': null }, 'prev': null }, 'prev': null }, 'prev': null } }'''
    print(actual)
    print(expected)
    assert expected == actual
*/
