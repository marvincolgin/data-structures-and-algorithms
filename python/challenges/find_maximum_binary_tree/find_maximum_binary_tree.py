import os,sys,inspect
cwd = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.insert(0, cwd)
sys.path.insert(0, cwd+'/../../data-structures/tree')

from tree import Node, BinaryTree, TraverseMethod


def find_maximum_value(tree, action_func):
