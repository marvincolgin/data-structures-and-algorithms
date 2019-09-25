import sys
sys.path.insert(0, '../../data-structures/hashtable')
sys.path.insert(0, '../../data-structures/tree')
sys.path.insert(0, '../../data-structures/linked_list')
from hashtable import HashTable  # noqa: 402
from tree import BinaryTree, TraverseMethod  # noqa: 402
import json  # noqa: 402


def tree_intersection(tree1, tree2: BinaryTree) -> list:
    # return an array with all the values in both tree1 and tree2
    # BigO Time==O(2n)  Space==0(1.3n) 30% for hashtable
    # assumption: No Duplicates within Trees

    # return early
    if not isinstance(tree1, BinaryTree) or not isinstance(tree2, BinaryTree):
        raise ValueError('Must pass BinaryTree for parameters.')
    if not tree1.root or not tree2.root:
        return []

    # init local vars
    ht = HashTable()
    retArray = []

    # callbacks for traversal of binary tree
    def _add(node):
        # used for the 1st tree to define a list of values
        ht.add(str(node.value), 1)

    def _add_isdup(node):
        # used for the 2nd tree, if its already there, then
        # its a candidate for return
        try:
            ht.add(str(node.value), 1)
        except ValueError:
            retArray.append(node.value)

    # Traverse through both trees, different callback func
    tree1.traverse(TraverseMethod.IN_ORDER, _add)
    tree2.traverse(TraverseMethod.IN_ORDER, _add_isdup)

    return retArray
