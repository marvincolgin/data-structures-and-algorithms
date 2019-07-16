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
        buf = ''
        ptr = self.head
        while ptr is not None:
            buf = buf + ptr.value + ','
            ptr = ptr.next
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

    def insertBefore(self, beforeThisVal: int, newVal: str):
        # add a new node wifith the given newValue immediately before the first value node
        # BigO == O(n)

        print(f'beforeThisVal:[{beforeThisVal}]')
        print(f'newVal:[{newVal}]')

        # Handle Base Case First
        if self.head is None:
            node = LinkNode(newVal)
            self.head = node
            return True

        # Handle: target is first entry
        if self.head.value == beforeThisVal:
            node = LinkNode(newVal)
            node.next = self.head
            self.head = node
            return True

        # Handle: traverse list, looking for value
        found = False
        ptr = self.head
        while ptr is not None:
            if ptr.next is not None and ptr.next.value == beforeThisVal:
                found = True
                break
            ptr = ptr.next
            # Insert *if* found
            if found:
                print(f'ptr.next.value:[{ptr.next.value}]')
                node = LinkNode(newVal)
                node.next = ptr.next
                ptr.next = node
                return True

        return False

    def insertAfter(self, value, newVal):
        # add a new node with the given newValue immediately after the first value node
        # BigO == O(n)
        pass


if __name__ == "__main__":
    ll = LinkList()
    ll.insert('2')
    ll.insert('3')
    ll.insert('1')
    ll.insertBefore('1', '4')
    print(ll.toStr())
