from enum import IntEnum

class TraverseMethod(IntEnum):
    IN_ORDER = 1
    PRE_ORDER = 2
    POST_ORDER = 3

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def traverse(self, method, action_func):

        def _visit(node):

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

    def returnAsArr(self, method):

        result = []

        def action_func(value):
            result.append(value)

        self.traverse(method, action_func)
        return(result)


class BinarySearchTree:
    pass
