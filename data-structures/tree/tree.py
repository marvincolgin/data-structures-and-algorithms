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

    def traverse(self, method):

        results = []

        def _visit(node):

            if method == TraverseMethod.PRE_ORDER:
               results.append(node.value)

            if node.left:
                _visit(node.left)

            if method == TraverseMethod.IN_ORDER:
               results.append(node.value)

            if node.right:
                _visit(node.right)

            if method == TraverseMethod.POST_ORDER:
               results.append(node.value)

        _visit(self.root)
        return results


class BinarySearchTree:
    pass
