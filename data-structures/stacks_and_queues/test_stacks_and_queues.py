import pytest
import sys
from stacks_and_queues import Stack


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


    """
* QUEUE: enqueue into a queue
* QUEUE: enqueue multiple values into a queue
* QUEUE: dequeue out of a queue the expected value
* QUEUE: peek into a queue, seeing the expected value
* QUEUE: empty a queue after multiple dequeues
* QUEUE: instantiate an empty queue
    """
