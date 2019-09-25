import os,sys,inspect
cwd = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.insert(0, cwd)
sys.path.insert(0, cwd+'/../../data-structures/tree')

from tree import Node, BinaryTree, TraverseMethod


def test_tree_find_max():
    tree = BinaryTree()
    node = Node(50)
    tree.root = node

    node = Node(25)
    tree.root.left = node

    node = Node(60)
    tree.root.right = node

    node = Node(30)
    tree.root.left.right = node

    b, v = tree.find_max(tree)

    assert b == True
    assert v == 60

def test_empty():
    tree = BinaryTree()
    b, v = tree.find_max(tree)
    assert b == False

    b,v = BinaryTree().find_max(None)
    assert b == False
