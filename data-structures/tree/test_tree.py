import pytest
import random
from tree import TraverseMethod, BinaryTree, Node, BinarySearchTree


def test_exists():
    assert BinaryTree
    assert Node

@pytest.fixture()
def tree():

    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    eight = Node(8)
    nine = Node(9)

    one.left = two
    one.right = three
    three.left = four
    three.right = five
    two.left = six
    six.right = seven
    seven.left = eight
    seven.right = nine

    arbol = BinaryTree()
    arbol.root = one

    return arbol

def test_fixture(tree):
    assert tree

def test_pre_order(tree):
    expected = [ 1, 2, 6, 7, 8, 9, 3, 4, 5 ]
    actual = tree.returnAsArr(TraverseMethod.PRE_ORDER)
    assert expected == actual


def test_in_order(tree):
    expected = [ 6, 8, 7, 9, 2, 1, 4, 3, 5 ]
    actual = tree.returnAsArr(TraverseMethod.IN_ORDER)
    assert expected == actual

def test_post_order(tree):
    expected = [ 8, 9, 7, 6, 2, 4, 5, 3, 1 ]
    actual = tree.returnAsArr(TraverseMethod.POST_ORDER)
    assert expected == actual

def test_exists():
    assert BinarySearchTree

def test_contains():
    tree = BinarySearchTree()
    tree.add(50)
    assert tree.contains(50)

def test_add_empty():
    tree = BinarySearchTree()
    tree.add("apple")
    assert tree.root.value == "apple"

def test_add_smaller():
    tree = BinarySearchTree()
    tree.add(50)
    tree.add(25)
    assert tree.root.value == 50
    assert tree.root.left.value == 25

def test_add_larger():
    tree = BinarySearchTree()
    tree.add(50)
    tree.add(75)
    assert tree.root.value == 50
    assert tree.root.right.value == 75

def test_not_contains():
    tree = BinarySearchTree()
    tree.add(50)
    assert not tree.contains(150)

def test_add_X_random():

    vals = []
    tree = BinarySearchTree()
    for j in range(50):

        # Generate a list of X elements (not duplicate)
        while True:
           x = str(random.randint(1,200))
           try:
               noused = vals.index(x)
           except:
               # No Found
               break

        vals.append(x)
        tree.add(x)

    actual = tree.returnAsArr(TraverseMethod.IN_ORDER)

    vals.sort()
    expected = vals

    assert expected == actual
