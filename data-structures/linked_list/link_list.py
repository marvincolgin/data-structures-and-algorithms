import json


# **********************************
class LinkNode():

    value = ''
    next = None
    prev = None

    def __init__(self, value, next=None, prev=None):
        # constructor
        self.value = value
        self.next = next
        self.prev = prev


# **********************************
class LinkList():

    head = None

    def __init__(self):
        # constructor
        self.head = None

    def toJSON(self):
        # dump object to JSON and return as String
        buf = json.dumps(self, default=lambda o: o.__dict__, indent=0, separators=(',', ': '))
        buf = buf.replace('\n', ' ').replace('\r', '')
        return buf

    def insert(self, value):
        # insert value at the head of the list
        node = LinkNode(value, self.head)
        node.next = self.head
        self.head = node

    def includes(self, value):
        # traverse list and determine if a value exists
        # return bool
        ret = False
        cur = self.head
        while cur is not None:
            if cur.value == value:
                ret = True
                break
            cur = cur.next
        return ret

    def count(self):
        # count the number of nodes and return count
        cnt = 0
        cur = self.head
        while cur is not None:
            cnt += 1
            cur = cur.next
        return cnt
