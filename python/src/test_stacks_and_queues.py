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
    actualBool, actualStr = stack.peek()
    expectedBool, expectedStr = True, 'pao de queijo'
    assert actualBool == expectedBool
    assert actualStr == expectedStr


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
    expectedBool = True
    expectedStr = 'banana'
    actualBool, actualStr = stack.peek()
    assert actualBool == expectedBool
    assert actualStr == expectedStr


def test_queue_classexists():
    assert Queue


def test_queue_cancreate():
    q = Queue()
    expected = True
    actual = isinstance(q, Queue)
    assert expected == actual


def helper_queue_enqueue_lots():
    q = Queue()
    q.enqueue('pao de queijo')
    q.enqueue('pappa sandwidh')
    q.enqueue('banana')
    q.enqueue('crackers')
    q.enqueue('strawberries')
    q.enqueue('chocolate chips')
    return q


def test_queue_enqueue():
    # enqueue into a queue
    q = Queue()
    q.enqueue('pao de queijo')
    assert q.count() == 1


def test_queue_enqueue_lots():
    # enqueue multiple values into a queue
    q = helper_queue_enqueue_lots()
    assert q.count() == 6


def test_queue_dequeue_success():
    # dequeue out of a queue the expected value
    q = helper_queue_enqueue_lots()
    expected = True
    actual = q.dequeue("banana")
    assert expected == actual

    expected = 5
    actual = q.count()
    assert expected == actual


def test_queue_dequeue_error():
    # dequeue out of a queue the expected value
    q = helper_queue_enqueue_lots()
    expected = False
    actual = q.dequeue("somethingyouwontfind")
    assert expected == actual

    expected = 6
    actual = q.count()
    assert expected == actual


def test_queue_peek():
    # peek into a queue, seeing the expected value
    q = helper_queue_enqueue_lots()
    actualBool, actualStr = q.peek()
    expectedBool = True
    assert actualBool == expectedBool
    expected = 'pao de queijo'
    assert expected == actualStr


def test_queue_peek_empty():
    # peek into a queue, seeing the expected value
    q = Queue()
    actualBool, actualStr = q.peek()
    expectedBool = False
    assert actualBool == expectedBool
    expected = ''
    assert expected == actualStr


def test_queue_dequeue_untilempty():
    # empty a queue after multiple dequeues
    q = helper_queue_enqueue_lots()
    arr = q.toStr().split(',')
    for x in arr:
        q.dequeue(x)
    assert q.count() == 0
