import pytest
import sys
from stacks_and_queues import Stack, Queue


def helper_stack_addlots():
    stack = Stack()
    stack.push('pao de queijo')
    stack.push('pappa sandwidh')
    stack.push('banana')
    return stack


def test_stack_cancreate():
    # STACK: instantiate an empty stack
    stack = Stack()
    expected = True
    actual = isinstance(stack, Stack)
    assert expected == actual


def test_stack_classexists():
    assert Stack()


def test_stack_push():
    # STACK: push onto a stack
    stack = Stack()
    stack.push('pao de queijo')
    actual = stack.peek()
    expected = 'pao de queijo'
    assert actual == expected


def test_stack_push_lots():
    # STACK: push multiple values onto a stack
    stack = helper_stack_addlots()
    expected = 3
    actual = stack.count()
    assert expected == actual


def test_stack_pop():
    # STACK: pop off the stack
    stack = helper_stack_addlots()
    expected = 'banana'
    actual = stack.pop()
    assert expected == actual
    assert stack.count() == 2


def test_stack_empty_after_pops():
    # STACK: empty a stack after multiple pops
    stack = helper_stack_addlots()
    for x in range(stack.count()-1):
        stack.pop()
    expected = 1
    actual = stack.count()
    assert expected == actual

    stack.pop()
    actual = stack.count()
    expected = 0
    assert expected == actual


def test_stack_peek():
    # STACK: peek the next item on the stack
    stack = helper_stack_addlots()
    expected = 'banana'
    actual = stack.peek()
    assert actual == expected


def test_queue_classexists():
    assert Queue


def test_queue_cancreate():
    q = Queue()
    expected = True
    actual = isinstance(q, Queue)
    assert expected == actual


def test_queue_enqueue():
    # enqueue into a queue
    pass

def test_queue_enqueue_lots():
    # enqueue multiple values into a queue
    pass


def test_queue_dequeue():
    # dequeue out of a queue the expected value
    pass


def test_queue_peek():
    # peek into a queue, seeing the expected value
    pass


def test_queue_dequeue_untilempty():
    # empty a queue after multiple dequeues
    pass




