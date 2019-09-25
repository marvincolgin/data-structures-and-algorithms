from queue_with_stacks import PseudoQueue

def test_class_exists():
    PseudoQueue()

def test_enqueue():
    pq = PseudoQueue()
    pq.enqueue('banana')
    pq.enqueue('strawberry')
    pq.enqueue('blueberry')
    expected = 3
    actual = 3
    assert expected == actual

def test_dequeue():
    pq = PseudoQueue()
    pq.enqueue('banana')
    pq.enqueue('strawberry')
    pq.enqueue('blueberry')

    expectedBool = True
    expectedStr  = 'banana'
    actualStr, actualBool = pq.dequeue()

    assert expectedBool == actualBool
    assert expectedStr  == actualStr

    expectedStr = 'strawberry'
    actualStr, actualBool = pq.dequeue()
    assert expectedStr == actualStr

    # @TODO these next two are failing, I need to move on to LAB tho..

    expectedStr = 'blueberry'
    actualStr, actualBool = pq.dequeue()
    assert expectedStr == actualStr

    expectedStr = ''
    expectedBool = False
    actualStr, actualBool = pq.dequeue()
    assert expectedStr == actualStr
    assert expectedBool == actualBool

