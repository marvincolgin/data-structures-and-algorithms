import os,sys,inspect
cwd = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.insert(0, cwd)
sys.path.insert(0, cwd+'/../../data-structures/tree')

from tree import Node, BinaryTree, TraverseMethod
from breadth_first import breadth_first
import pytest


# global variable to hold the 'output' of the function
# for comparison in test
pytest.retval = ''


def test_func_exists():
    breadth_first(None, None)


def action_func(val):
    pytest.retval = pytest.retval + str(val) + ', '


def test_breadth_first():
    tree = BinaryTree()
    node = Node(50)
    tree.root = node

    node = Node(25)
    tree.root.left = node

    node = Node(60)
    tree.root.right = node

    node = Node(30)
    tree.root.left.right = node

    breadth_first(tree, action_func)


    # slice off the ', ' at the end
    actual = pytest.retval[:-2]

    expected = '50, 25, 60, 30'

    assert actual == expected

def test_breadth_empty():
    breadth_first(BinaryTree(), action_func)
