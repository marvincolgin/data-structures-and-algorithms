from enum import IntEnum

class TraverseMethod(IntEnum):
    # enum class for traversal and processing order
    IN_ORDER = 1
    PRE_ORDER = 2
    POST_ORDER = 3


class Node:
    # class for nodes within Tree

    def __init__(self, value):
        # constructor for creating Node
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        # constructor for creating BinaryTree
        self.root = None

    def traverse(self, method : TraverseMethod, action_func):
        # visit each node in atree, using a specified method and call action_func() for each node

        def _visit(node):
            # recusive function for visiting each node

            if method == TraverseMethod.PRE_ORDER:
                action_func(node.value)

            if node.left:
                _visit(node.left)

            if method == TraverseMethod.IN_ORDER:
                action_func(node.value)

            if node.right:
                _visit(node.right)

            if method == TraverseMethod.POST_ORDER:
                action_func(node.value)

        _visit(self.root)

    def returnAsArr(self, method : TraverseMethod):
        # return the enter tree as an array using a specified method

        result = []

        def action_func(value):
            result.append(value)

        self.traverse(method, action_func)
        return(result)


class BinarySearchTree(BinaryTree):
    # class for binary-search-tree

    def add(self, new_value):
        # adds new value to the tree

        def _find_and_insert(node):
            # recursive method for evaluating a node and calling itself depending on the value

            if node.value > new_value:
                if node.left is None:
                    node.left = Node(new_value)
                else:
                    _find_and_insert(node.left)
            if node.value < new_value:
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

            if node.value == target_value:
                return True
            if node.value > target_value:
                if node.left is None:
                    return False
                else:
                    _visit(node.left)
            if node.value < target_value:
                if node.right is None:
                    return False
                else:
                    _visit(node.right)

        return _visit(self.root)

