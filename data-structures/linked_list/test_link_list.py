from link_list import LinkList, LinkNode


def helper_insert_many(ll):
    ll.insert('0')
    ll.insert('1')
    ll.insert('2')
    ll.insert('3')
    ll.insert('4')
    ll.insert('5')
    ll.insert('6')
    ll.insert('7')
    ll.insert('8')
    ll.insert('9')


def test_class_exists():
    assert LinkList
    assert LinkNode


def test_count():
    ll = LinkList()
    helper_insert_many(ll)
    expected = 10
    actual = ll.count()
    assert actual == expected


def test_insert():
    ll = LinkList()
    ll.insert('one')
    assert ll.head.value == 'one'


def test_insert_many():
    ll = LinkList()
    helper_insert_many(ll)
    assert ll.count() == 10
    assert ll.head.value == '9'
    assert ll.head.next.value == '8'
    assert ll.head.next.next.value == '7'
    assert ll.head.next.next.next.value == '6'
    assert ll.head.next.next.next.next.value == '5'
    assert ll.head.next.next.next.next.next.value == '4'
    assert ll.head.next.next.next.next.next.next.value == '3'
    assert ll.head.next.next.next.next.next.next.next.value == '2'
    assert ll.head.next.next.next.next.next.next.next.next.value == '1'
    assert ll.head.next.next.next.next.next.next.next.next.next.value == '0'
    assert ll.head.next.next.next.next.next.next.next.next.next.next is None


def test_includes():
    ll = LinkList()
    helper_insert_many(ll)
    expected = True
    actual = ll.includes('5')
    assert expected == actual


def test_includes_notfound():
    ll = LinkList()
    helper_insert_many(ll)
    expected = False
    actual = ll.includes('five')
    assert expected == actual


def test_toJSON():
    # Dump the LinkList to JSON and compare to what it should be
    ll = LinkList()
    helper_insert_many(ll)
    actual = ll.toJSON()
    expected = """{ "head": { "value": "9", "next": { "value": "8", "next": { "value": "7", "next": { "value": "6", "next": { "value": "5", "next": { "value": "4", "next": { "value": "3", "next": { "value": "2", "next": { "value": "1", "next": { "value": "0", "next": null, "prev": null }, "prev": null }, "prev": null }, "prev": null }, "prev": null }, "prev": null }, "prev": null }, "prev": null }, "prev": null }, "prev": null } }"""
    print(actual)
    print(expected)
    assert expected == actual


def test_append():
    ll = LinkList()
    ll.insert('2')
    ll.insert('3')
    ll.insert('1')
    ll.append('5')
    expected = '1,3,2,5'
    actual = ll.toStr()
    assert expected == actual


def helper_insertBefore():
    ll = LinkList()
    ll.insert('2')
    ll.insert('3')
    ll.insert('1')
    return ll


def test_insertBefore():
    #ll = helper_insertBefore()
    #ll.insertBefore('3', '4')
    #expected = '1,4,3,2'
    #actual = ll.toStr()
    #assert expected == actual

    #ll = helper_insertBefore()
    #ll.insertBefore(1, 5)

    #ll = helper_insertBefore()
    #ll.insertBefore(2, 5)

    #ll = helper_insertBefore()
    #ll.insertBefore(4, 5)
    #** exception
    pass


"""
def test_insertAfter()
    ll = helper_insertBefore()
    ll.insertAfter(3, 5)

    ll.insertAfter(2, 5

    ll.insertAfter(4, 5
    Exception
"""