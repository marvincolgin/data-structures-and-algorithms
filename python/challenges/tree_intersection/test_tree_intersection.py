import pytest
import sys
sys.path.insert(0, '../../data-structures/tree')
from tree import BinaryTree, Node  # noqa: 402
from tree_intersection import tree_intersection  # noqa: 402


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


def test_func_emptytree():
    tree1 = BinaryTree()
    tree2 = BinaryTree()

    expected = []
    actual = tree_intersection(tree1, tree2)


def test_func_invalidparams():
    with pytest.raises(ValueError):
        tree_intersection(None, None)


def test_func_matches_allofit(tree):

    tree1 = tree
    tree2 = tree1

    expected = [6, 8, 7, 9, 2, 1, 4, 3, 5]
    actual = tree_intersection(tree1, tree2)
    assert expected == actual


def test_func_match_none(tree):

    tree1 = tree
    tree2 = BinaryTree()

    expected = []
    actual = tree_intersection(tree1, tree2)
    assert expected == actual


def test_func_match_some(tree):

    tree1 = tree
    tree2 = BinaryTree()
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
    two.left = six
    six.right = seven
    seven.left = eight
    tree2.root = one

    expected = [6, 8, 7, 2, 1, 4, 3]
    actual = tree_intersection(tree1, tree2)
    assert expected == actual
