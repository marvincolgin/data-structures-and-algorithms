import os,sys,inspect
cwd = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.insert(0, cwd)
sys.path.insert(0, cwd+'/../../data-structures/tree')

from tree import BinaryTree, TraverseMethod


def fizz_buzz_valueswitch(node):

    if node is None:
        return

    if node.value % 5 == 0 and node.value % 3 == 0:
        node.value = 'FizzBuzz'
    elif node.value % 5 == 0:
        node.value = 'Buzz'
    elif node.value % 3 == 0:
        node.value = 'Fizz'


def fizz_buzz_tree(tree : BinaryTree) -> BinaryTree:

    # Base Case
    if tree is None or tree.root is None:
        return tree

    # Great Helper func, that I built into the class to traverse and do something on each node
    tree.traverse(TraverseMethod.IN_ORDER, fizz_buzz_valueswitch)

    return tree

