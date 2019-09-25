import os,sys,inspect
cwd = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.insert(0, cwd)
sys.path.insert(0, cwd+'/../../data-structures/tree')

from tree import Node, BinaryTree, TraverseMethod
from fizz_buzz_tree import fizz_buzz_tree


def test_func_exists():
    fizz_buzz_tree(None)


def test_fizz_buzz_tree_all():
    tree = BinaryTree()
    node = Node(50)
    tree.root = node

    node = Node(25)
    tree.root.left = node

    node = Node(60)
    tree.root.right = node

    node = Node(30)
    tree.root.left.right = node
    fizz_buzz_tree(tree)

    arr = tree.returnAsArr(TraverseMethod.IN_ORDER)
    actual = f'{arr}'
    expected = "['Buzz', 'FizzBuzz', 'Buzz', 'FizzBuzz']"

    assert actual == expected


def test_fizz_buzz_empty():
    tree = BinaryTree()

    tree = fizz_buzz_tree(tree)

    actual = isinstance(tree, BinaryTree)
    expected = True

    assert actual == expected


def test_fizz_buzz_tree_none():
    tree = BinaryTree()
    node = Node(49)
    tree.root = node

    node = Node(23)
    tree.root.left = node

    node = Node(61)
    tree.root.right = node

    node = Node(31)
    tree.root.left.right = node
    fizz_buzz_tree(tree)

    arr = tree.returnAsArr(TraverseMethod.IN_ORDER)
    actual = f'{arr}'
    expected = "[23, 31, 49, 61]"

    assert actual == expected
