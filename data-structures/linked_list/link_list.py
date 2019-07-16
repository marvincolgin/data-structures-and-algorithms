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

    def toStr(self):
        # dump list as simple text-list

        # c,cnt are limiters to make sure we don't go run away
        # yes, we need cnt=self.count() and not -1, as we walk off list
        c, cnt = 0, self.count()
        buf = ''
        ptr = self.head
        while ptr is not None:
            buf = buf + ptr.value + ','
            ptr = ptr.next
            c += 1
            if (c > cnt):
                raise AssertionError(f'WAIT!!! Forever Loop!\nRecursive LinkList/Node\nbuf:[{buf}]')

        if buf.endswith(','):
            buf = buf[:-1]
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

    def append(self, value):
        # adds a new node with the given value to the end of the list
        # BigO == O(n)

        # walk to end of list
        prev, cur = None, self.head
        while cur is not None:
            prev = cur
            cur = cur.next

        # create the node and add it to the end
        node = LinkNode(value, None)
        prev.next = node

        return True

    def insertBefore(self, targetVal: int, newVal: str, afterInstead=False):
        # add a new node with the given newValue immediately BEFORE the node containg targetVal
        # note: this bevahoir can be modified by the bool afterInstead
        # BigO == O(n)

        # walk the list to find it or the end
        found = False
        prev, cur = None, self.head
        while cur is not None:
            if cur.value == targetVal:
                found = True
                break
            prev = cur
            cur = cur.next

        # if found, put it in the chain, as a link right before the node containing value
        if found:
            node = LinkNode(newVal)
            if afterInstead:
                node.next = cur.next
                cur.next = node
            else:
                node.next = cur
                if prev is None: # edge-case, if the targetVal is first node
                    self.head = node
                else:
                    prev.next = node

        return found

    def insertAfter(self, targetVal: int, newVal: str):
        # add a new node with the given newValue immediately AFTER the node containg targetVal
        # BigO == O(n)
        return self.insertBefore(self, targetVal, newVal, True)


if __name__ == "__main__":
    ll = LinkList()
    ll.insert('2')
    ll.insert('3')
    ll.insert('1')
    ll.insertBefore('1', '4')
    print(ll.toStr())
