var chai = require('chai');
var expect = chai.expect; // we are using the 'expect' style of Chai

var Node = require('./tree').Node
var BinaryTree = require('./tree').BinaryTree
var BinarySearchTree = require('./tree').BinarySearchTree
var TraverseMethod = require('./tree').TraverseMethod
var ComparisonSign = require('./tree').ComparisonSign

function HelperTreeAddLots() {
    one = new Node(1)
    two = new Node(2)
    three = new Node(3)
    four = new Node(4)
    five = new Node(5)
    six = new Node(6)
    seven = new Node(7)
    eight = new Node(8)
    nine = new Node(9)

    one.left = two
    one.right = three
    three.left = four
    three.right = five
    two.left = six
    six.right = seven
    seven.left = eight
    seven.right = nine

    tree = new BinaryTree()
    tree.root = one

    return tree
}

describe('BinaryTree', function() {
   it('new BinaryTree()', function() {
      expect(new BinaryTree()).to.be.instanceOf(BinaryTree)
   })
   it('traverse(PRE_ORDER)', function() {
      bt = HelperTreeAddLots()
      expected = [1, 2, 6, 7, 8, 9, 3, 4, 5]
      expect(bt.returnAsArr(TraverseMethod.PRE_ORDER)).to.be.eql(expected)
   })
   it('traverse(IN_ORDER)', function() {
      bt = HelperTreeAddLots()
      expected = [6, 8, 7, 9, 2, 1, 4, 3, 5]
      expect(bt.returnAsArr(TraverseMethod.IN_ORDER)).to.be.eql(expected)
   })
   it('traverse(POST_ORDER)', function() {
      bt = HelperTreeAddLots()
      expected = [8, 9, 7, 6, 2, 4, 5, 3, 1]
      expect(bt.returnAsArr(TraverseMethod.POST_ORDER)).to.be.eql(expected)
   })
})
describe('BinarySearchTree', function() {
   it('new BinarySearchTree()', function() {
      expect(new BinarySearchTree()).to.be.instanceOf(BinarySearchTree)
   })
   it('contains()', function() {
      tree = new BinarySearchTree()
      tree.add(50)
      expect(tree.contains(50)).to.be.true
   })
   it('add()::empty', function() {
      tree = new BinarySearchTree()
      tree.add('apple')
      expect(tree.root.value).to.be.equal('apple')
   })
   it('add()::smaller', function() {
      tree = new BinarySearchTree()
      tree.add(50)
      tree.add(25)
      expect(tree.root.value).to.be.equal(50)
      expect(tree.root.left.value).to.be.equal(25)
   })
   it('add()::larger', function() {
      tree = new BinarySearchTree()
      tree.add(50)
      tree.add(75)
      expect(tree.root.value).to.be.equal(50)
      expect(tree.root.right.value).to.be.equal(75)
   })
   it('contains()::FALSE', function() {
      tree = new BinarySearchTree()
      tree.add(50)
      expect(tree.contains(150)).to.be.false
   })
   it('comparison_func_default()', function() {
      tree = new BinarySearchTree()
      tree.add('1')
      tree.add('11')
      tree.add('111')
      tree.add('2')
      tree.add('22')
      tree.add('222')
      tree.add('3')
      tree.add('33')
      tree.add('333')
      expected = [ '1', '11', '111', '2', '22', '222', '3', '33', '333']
      expect(tree.returnAsArr(TraverseMethod.IN_ORDER)).to.be.eql(expected)
   })
   it('comparison_func_userdef()', function() {

      var _comparison_func_userdef = (val1, val2, CS) => {
         if (CS == ComparisonSign.EQUAL) {
            return parseInt(val1) == parseInt(val2)
         }
         else
         if (CS == ComparisonSign.LESS) {
            return parseInt(val1) < parseInt(val2)
         }
         else
         if (CS == ComparisonSign.GREATER) {
            return parseInt(val1) > parseInt(val2)
         }
         else
            return false
      }
      tree = new BinarySearchTree(_comparison_func_userdef)
      tree.add('1')
      tree.add('11')
      tree.add('111')
      tree.add('2')
      tree.add('22')
      tree.add('222')
      tree.add('3')
      tree.add('33')
      tree.add('333')
      expected = [ '1', '2', '3', '11', '22', '33', '111', '222', '333' ]
      actual = tree.returnAsArr(TraverseMethod.IN_ORDER)
      expect(actual).to.be.eql(expected)
   })
   it('add_x_random()', function() {
      vals = []
      tree = new BinarySearchTree()
      for (let j=0; j<50; j++) {
         while (true) {
            x = Math.random()
            if (!vals.includes(x)) {
               break
            }
         }
         vals.push(x)
         tree.add(x)
      }

      actual = tree.returnAsArr(TraverseMethod.IN_ORDER)

      vals.sort()
      expected = vals

      expect(actual).to.be.eql(expected)
   })
})
