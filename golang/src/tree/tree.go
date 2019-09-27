package tree

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

// BinaryTree implementation
type BinaryTree struct {
	root *Node
}

// Init of Binary Tree
func (tree *BinaryTree) Init() {
	tree.root = nil
}

// Traverse of BinaryTree
func (tree *BinaryTree) Traverse(method int, actionFunc func(val interface{})) {

	var _visit = func(node *Node) {
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
func (tree *BinaryTree) ReturnAsArr(method int) []interface{} {

	var retval []interface{} = make([]interface{}, 0)

	actionFunc := func(value interface{}) {
		retval = append(retval, value)
	}

	tree.Traverse(method, actionFunc)

	return retval
}

/*

class BinaryTree:


    def traverse(self, method : TraverseMethod, action_func):
        # visit each node in atree, using a specified method and call action_func() for each node

        def _visit(node):
            # recusive function for visiting each node

            if method == TraverseMethod.PRE_ORDER:
                action_func(node)

            if node.left:
                _visit(node.left)

            if method == TraverseMethod.IN_ORDER:
                action_func(node)

            if node.right:
                _visit(node.right)

            if method == TraverseMethod.POST_ORDER:
                action_func(node)

        _visit(self.root)

    def returnAsArr(self, method : TraverseMethod):
        # return the enter tree as an array using a specified method

        result = []

        def action_func(node):
            result.append(node.value)

        self.traverse(method, action_func)
        return(result)

    @staticmethod
    # arg:tree should have type-hinting, but ZEIT::now has issues with Python 3.6
    def find_max(tree) -> (bool,int):
        # return the largest integer in treee

        retBool = False
        retVal  = -1


        def action_func(node):
            nonlocal retVal
            if node.value > retVal:
                retVal = node.value

        if tree and tree.root:
            retBool = True
            retVal = tree.root.value

            tree.traverse(TraverseMethod.IN_ORDER, action_func)

        return retBool, retVal


class BinarySearchTree(BinaryTree):
    # class for binary-search-tree

    comparison_func = None

    def comparison_func_default(self, val1, val2, CS : ComparisonSign):
        # default comparison function

        if CS == ComparisonSign.EQUAL:
            return val1 == val2
        if CS == ComparisonSign.LESS:
            return val1 < val2
        if CS == ComparisonSign.GREATER:
            return val1 > val2
        return False  # Never get here

    def __init__(self, comparison_func=None):
        BinaryTree.__init__(self)

        if comparison_func:
            self.comparison_func = comparison_func
        else:
            self.comparison_func = self.comparison_func_default

    def add(self, new_value):
        # adds new value to the tree

        def _find_and_insert(node):
            # recursive method for evaluating a node and calling itself depending on the value

            if self.comparison_func(node.value, new_value, ComparisonSign.GREATER):
                # if node.value > new_value:
                if node.left is None:
                    node.left = Node(new_value)
                else:
                    _find_and_insert(node.left)

            if self.comparison_func(node.value, new_value, ComparisonSign.LESS):
                # if node.value < new_value:
                if node.right is None:
                    node.right = Node(new_value)
                else:
                    _find_and_insert(node.right)

        if self.root is None:
            self.root = Node(new_value)
        else:
          _find_and_insert(self.root)

    def contains(self, target_value) -> bool:
        # accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once.

        def _visit(node):
            # recursive function for isiting each node

            if self.comparison_func(node.value, target_value, ComparisonSign.EQUAL):
                # if node.value == target_value:
                return True
            if self.comparison_func(node.value, target_value, ComparisonSign.GREATER):
                # if node.value > target_value:
                if node.left is None:
                    return False
                else:
                    _visit(node.left)
            if self.comparison_func(node.value, target_value, ComparisonSign.LESS):
                # if node.value < target_value:
                if node.right is None:
                    return False
                else:
                    _visit(node.right)

        if self.root is not None:
            return _visit(self.root)
        else:
            return False

*/
