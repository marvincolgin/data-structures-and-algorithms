from __future__ import annotations
from enum import IntEnum

class TraverseMethod(IntEnum):
    # enum class for traversal and processing order
    IN_ORDER = 1
    PRE_ORDER = 2
    POST_ORDER = 3

class ComparisonSign(IntEnum):
    # enum class for comparisons, gt, lt and equal
    LESS = 1
    GREATER = 2
    EQUAL = 3

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
    def find_max(tree : BinaryTree) -> (bool,int):
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

        print(f'comp_default() val1:[{val1}] val2:[{val2}] cs:[{CS}]')

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

        return _visit(self.root)

