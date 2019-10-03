package tree

import (
	"fmt"
	"os"
)

const (
	// TraversalOrderPre left->middle->right order
	TraversalOrderPre = iota
	// TraversalOrderIn middle->left->right order
	TraversalOrderIn = iota
	// TraversalOrderPost left->right->middle order
	TraversalOrderPost = iota
)

const (
	// ComparisonSignLess is the literal Less-Than Sign
	ComparisonSignLess = iota
	// ComparisonSignGreater is the literal Greater-Than Sign
	ComparisonSignGreater = iota
	// ComparisonSignEqual is the literal Equal Sign
	ComparisonSignEqual = iota
)

// Node for Tree
type Node struct {
	Val   interface{}
	left  *Node
	right *Node
}

// NewNode constructor for Node
func NewNode(val interface{}) Node {
	return Node{val, nil, nil}
}

// BinarySearchTree implementation
type BinarySearchTree struct {
	root           *Node
	comparisonFunc func(val1 interface{}, val2 interface{}, CS int) bool
}

// NewBinarySearchTree of Binary Tree
func NewBinarySearchTree(comparisonFunc func(val1 interface{}, val2 interface{}, CS int) bool) BinarySearchTree {
	t := BinarySearchTree{nil, nil}
	if comparisonFunc == nil {
		t.comparisonFunc = t.comparisonFuncDefault
	} else {
		t.comparisonFunc = comparisonFunc
	}
	return t
}

// Traverse of BinarySearchTree
func (tree *BinarySearchTree) Traverse(method int, actionFunc func(val interface{})) {

	// formally defining the var to the func, will allow us to call-ourselves
	var _visit func(node *Node)

	_visit = func(node *Node) {
		if method == TraversalOrderPre {
			actionFunc(node.Val)
		}

		if node.left != nil {
			_visit(node.left)
		}

		if method == TraversalOrderIn {
			actionFunc(node.Val)
		}

		if node.right != nil {
			_visit(node.right)
		}

		if method == TraversalOrderPost {
			actionFunc(node.Val)
		}
	}

	if tree.root != nil {
		_visit(tree.root)
	}

}

// ReturnAsArr will return the tree as as array
func (tree *BinarySearchTree) ReturnAsArr(method int) []interface{} {

	var retval []interface{} = make([]interface{}, 0)

	actionFunc := func(value interface{}) {
		retval = append(retval, value)
	}

	tree.Traverse(method, actionFunc)

	return retval
}

// comparison_func_default is the default of comparing values
func (tree *BinarySearchTree) comparisonFuncDefault(val1 interface{}, val2 interface{}, CS int) bool {
	if CS == ComparisonSignEqual {
		return val1.(string) == val2.(string)
	} else if CS == ComparisonSignLess {
		return val1.(string) < val2.(string)
	} else if CS == ComparisonSignGreater {
		return val1.(string) > val2.(string)
	} else {
		return false
	}
}

// findAndInsert recursive method for evaluating a node and calling itself depending on the value
func (tree *BinarySearchTree) findAndInsert(node *Node, newValue interface{}) {

	if tree.comparisonFunc == nil {
		fmt.Printf("ERROR! tree.comparisonFunc==nil")
		os.Exit(99)
	}

	if tree.comparisonFunc(node.Val, newValue, ComparisonSignGreater) {
		if node.left == nil {
			node.left = &Node{newValue, nil, nil}
		} else {
			tree.findAndInsert(node.left, newValue)
		}
	}

	if tree.comparisonFunc(node.Val, newValue, ComparisonSignLess) {
		if node.right == nil {
			node.right = &Node{newValue, nil, nil}
		} else {
			tree.findAndInsert(node.right, newValue)
		}
	}
}

// Add a value to the Tree
func (tree *BinarySearchTree) Add(newValue interface{}) {

	if tree.root == nil {
		node := Node{newValue, (*Node)(nil), (*Node)(nil)}
		tree.root = &node
	} else {
		tree.findAndInsert(tree.root, newValue)
	}

}

// Contains accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once.
func (tree *BinarySearchTree) Contains(targetVal interface{}) bool {

	// *** Return Early
	if tree.root == nil {
		return false
	}

	if tree.comparisonFunc == nil {
		fmt.Printf("ERROR! tree.comparisonFunc==nil")
		os.Exit(99)
	}

	var _visit func(node *Node) bool

	_visit = func(node *Node) bool {

		if tree.comparisonFunc(node.Val, targetVal, ComparisonSignEqual) {
			return true
		}
		if tree.comparisonFunc(node.Val, targetVal, ComparisonSignGreater) {
			if node.left == nil {
				return false
			}
			_visit(node.left)
		}
		if tree.comparisonFunc(node.Val, targetVal, ComparisonSignLess) {
			if node.right == nil {
				return false
			}
			_visit(node.right)
		}
		return false
	}

	return _visit(tree.root)
}
