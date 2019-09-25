import os,sys,inspect
cwd = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.insert(0, cwd)
sys.path.insert(0, cwd+'/../../data-structures/tree')
sys.path.insert(0, cwd+'/../../data-structures/stacks_and_queues')
sys.path.insert(0, cwd+'/../../data-structures/linked_list')

from stacks_and_queues import Queue
from tree import Node, BinaryTree, TraverseMethod


def breadth_first(tree, action_func):

    # early return if empty tree
    if tree is None or tree.root is None:
        return

    q = Queue()
    q.enqueue(tree.root)

    while True:
        b, node = q.peek()
        if b == False:
            break

        q.dequeue(node)

        if node.left:
            q.enqueue(node.left)

        if node.right:
            q.enqueue(node.right)

        action_func(node.value)
