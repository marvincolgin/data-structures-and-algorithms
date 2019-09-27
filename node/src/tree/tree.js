// enum class for traversal and processing order
var TraverseMethod = {
   PRE_ORDER: 1,
   IN_ORDER: 2,
   POST_ORDER: 3
}

// enum class for comparisons, gt, lt and equal
var ComparisonSign = {
    LESS: 1,
    GREATER: 2,
    EQUAL: 3
}

// class for nodes within Tree
class Node {
   constructor(value) {
      this.value = value
      this.left = null
      this.right = null
   }
}

// BinaryTree Implementation
class BinaryTree {

   constructor() {
      this.root = null
   }

   traverse(method, action_func) {

      function _visit(node) {
         if (method == TraverseMethod.PRE_ORDER) {
            action_func(node.value)
         }

         if (node.left) {
            _visit(node.left)
         }

         if (method == TraverseMethod.IN_ORDER) {
            action_func(node.value)
         }

         if (node.right) {
            _visit(node.right)
         }

         if (method == TraverseMethod.POST_ORDER) {
            action_func(node.value)
         }
      }

      _visit(this.root)
   }

   returnAsArr(method) {
      let result = []

      this.traverse(method, function(value) {
         result.push(value)
      })

      return result
   }
}

class BinarySearchTree extends BinaryTree {

   constructor(comparison_func=null) {
      super()

      if (comparison_func == null) {
         this.comparison_func = this.comparison_func_default
      } else {
         this.comparison_func = comparison_func
      }
   }

   //  default comparison function
   comparison_func_default(val1, val2, CS) {
      if (CS == ComparisonSign.EQUAL) {
         return val1 == val2
      }
      else
      if (CS == ComparisonSign.LESS) {
         return val1 < val2
      }
      else
      if (CS == ComparisonSign.GREATER) {
         return val1 > val2
      }
      else {
         return false  // Never get here
      }
   }

   // adds new value to the tree
   add(new_value) {

      // recursive method for evaluating a node and calling itself depending on the value
      // @TO-RESEARCH:  see how an arrow-function is used to access the "this", learn more!
      var _find_and_insert = (node) => {

         if (this.comparison_func(node.value, new_value, ComparisonSign.GREATER))
               if (node.left == null) {
                  node.left = new Node(new_value)
               } else {
                  _find_and_insert(node.left)
               }

         if (this.comparison_func(node.value, new_value, ComparisonSign.LESS))
               if (node.right == null) {
                  node.right = new Node(new_value)
               } else {
                  _find_and_insert(node.right)
               }
      }

      if (this.root == null) {
         this.root = new Node(new_value)
      } else {
         _find_and_insert(this.root)
      }
   }

   // accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once.
   contains(target_value) {

      // recursive function for isiting each node
      // @TO-RESEARCH:  see how an arrow-function is used to access the "this", learn more!
      var _visit = (node) => {
         if (this.comparison_func(node.value, target_value, ComparisonSign.EQUAL))
               return true
         if (this.comparison_func(node.value, target_value, ComparisonSign.GREATER))
               if (node.left == null) {
                  return false
               } else {
                  _visit(node.left)
               }
         if (this.comparison_func(node.value, target_value, ComparisonSign.LESS))
               if (node.right == null) {
                  return false
               } else {
                  _visit(node.right)
               }
      }

      if (this.root != null) {
         return _visit(this.root)
      } else {
         return false
      }

   }

}

module.exports.Node = Node
module.exports.BinaryTree = BinaryTree
module.exports.BinarySearchTree = BinarySearchTree
module.exports.TraverseMethod = TraverseMethod
module.exports.ComparisonSign = ComparisonSign
